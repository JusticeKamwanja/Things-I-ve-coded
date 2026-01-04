"""Text-to-Speech app using customtkinter + pygame + pyttsx3

Features:
- Enter text, play it back, and save audio to disk
- Uses `pyttsx3` to synthesize speech (offline)
- Uses `pygame.mixer` to play audio files
- Logs saved entries to `tts_logs.json` in `audio_data/`

Note: Install dependencies if missing:
    pip install customtkinter pygame pyttsx3
"""
import customtkinter as ctk
import pyttsx3
import pygame
import tempfile
import json
import os
from pathlib import Path
import datetime
from tkinter import filedialog, messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

DATA_DIR = Path("audio_data")
DATA_DIR.mkdir(exist_ok=True)
LOG_FILE = DATA_DIR / "tts_logs.json"

def append_log(record: dict):
    logs = []
    if LOG_FILE.exists():
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                logs = json.load(f)
        except Exception:
            logs = []
    logs.append(record)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2)

class TTSApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("TTS Studio — write, listen, save")
        self.geometry("820x520")

        # Initialize engines
        self.engine = pyttsx3.init()
        pygame.mixer.init()

        # UI
        self._build_ui()

        # Temp file holder
        self.temp_file = None

    def _build_ui(self):
        frame = ctk.CTkFrame(self)
        frame.pack(fill="both", expand=True, padx=16, pady=12)

        header = ctk.CTkLabel(frame, text="TTS Studio", font=("Helvetica", 20, "bold"))
        header.pack(pady=(0, 8))

        top_row = ctk.CTkFrame(frame)
        top_row.pack(fill="x", pady=(0, 8))

        self.voice_var = ctk.StringVar(value="default")
        voices = self.engine.getProperty("voices")
        self.voice_map = {v.name: v.id for v in voices}

        ctk.CTkLabel(top_row, text="Voice:").pack(side="left", padx=(6,4))
        self.voice_menu = ctk.CTkComboBox(top_row, values=list(self.voice_map.keys()), variable=self.voice_var)
        self.voice_menu.pack(side="left", padx=(0,12))

        self.rate_var = ctk.IntVar(value=self.engine.getProperty("rate"))
        ctk.CTkLabel(top_row, text="Rate:").pack(side="left", padx=(6,4))
        self.rate_slider = ctk.CTkSlider(top_row, from_=80, to=300, number_of_steps=44, command=self._on_rate_change)
        self.rate_slider.set(self.rate_var.get())
        self.rate_slider.pack(side="left", padx=(0,12), fill="x", expand=True)

        # Text area
        self.textbox = ctk.CTkTextbox(frame, height=260, fg_color="#1f1f1f", text_color="#eaeaea")
        self.textbox.pack(fill="both", expand=False, pady=(6,8))

        controls = ctk.CTkFrame(frame)
        controls.pack(fill="x")

        play_btn = ctk.CTkButton(controls, text="▶ Play", width=120, command=self.play_text)
        play_btn.pack(side="left", padx=6)

        stop_btn = ctk.CTkButton(controls, text="■ Stop", width=120, command=self.stop_audio)
        stop_btn.pack(side="left", padx=6)

        save_btn = ctk.CTkButton(controls, text="💾 Save as WAV", fg_color="#4CAF50", hover_color="#45a049", command=self.save_audio)
        save_btn.pack(side="left", padx=6)

        clear_btn = ctk.CTkButton(controls, text="✖ Clear", fg_color="#f44336", hover_color="#da190b", command=self.clear_text)
        clear_btn.pack(side="left", padx=6)

        spacer = ctk.CTkLabel(controls, text="")
        spacer.pack(side="left", expand=True)

        self.status_label = ctk.CTkLabel(controls, text="Ready", anchor="e")
        self.status_label.pack(side="right")

    def _on_rate_change(self, value):
        self.rate_var.set(int(float(value)))

    def _prepare_engine(self):
        # Apply selected voice and rate
        vname = self.voice_var.get()
        if vname in self.voice_map:
            try:
                self.engine.setProperty("voice", self.voice_map[vname])
            except Exception:
                pass
        self.engine.setProperty("rate", self.rate_var.get())

    def synth_to_file(self, text: str, path: Path):
        self._prepare_engine()
        # pyttsx3 can write directly to file
        try:
            self.engine.save_to_file(text, str(path))
            self.engine.runAndWait()
            return True
        except Exception as e:
            print("TTS save error:", e)
            return False

    def play_text(self):
        text = self.textbox.get("1.0", "end").strip()
        if not text:
            messagebox.showwarning("Empty", "Please enter some text to play.")
            return

        # create temporary wav file
        fd, tmp_path = tempfile.mkstemp(suffix=".wav", prefix="tts_")
        os.close(fd)
        tmp_path = Path(tmp_path)

        ok = self.synth_to_file(text, tmp_path)
        if not ok:
            messagebox.showerror("Error", "Failed to synthesize speech.")
            try:
                tmp_path.unlink(missing_ok=True)
            except Exception:
                pass
            return

        # play via pygame
        try:
            if pygame.mixer.get_init() is None:
                pygame.mixer.init()
            pygame.mixer.music.load(str(tmp_path))
            pygame.mixer.music.play()
            self.temp_file = tmp_path
            self.status_label.configure(text="Playing…")
            # monitor playback in background via event queue is possible, but we'll poll
            self.after(200, self._check_playback)
        except Exception as e:
            messagebox.showerror("Playback Error", str(e))

    def _check_playback(self):
        if pygame.mixer.music.get_busy():
            self.after(200, self._check_playback)
        else:
            self.status_label.configure(text="Ready")
            # cleanup temp
            if self.temp_file and self.temp_file.exists():
                try:
                    self.temp_file.unlink()
                except Exception:
                    pass
                self.temp_file = None

    def stop_audio(self):
        try:
            pygame.mixer.music.stop()
            self.status_label.configure(text="Stopped")
        except Exception:
            pass

    def save_audio(self):
        text = self.textbox.get("1.0", "end").strip()
        if not text:
            messagebox.showwarning("Empty", "Please enter some text to save.")
            return

        # Ask where to save
        initial = str(DATA_DIR / f"tts_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.wav")
        path = filedialog.asksaveasfilename(defaultextension=".wav", initialfile=Path(initial).name, filetypes=[("WAV files","*.wav")])
        if not path:
            return

        out_path = Path(path)
        ok = self.synth_to_file(text, out_path)
        if ok:
            record = {
                "timestamp": datetime.datetime.now().isoformat(),
                "file": str(out_path.resolve()),
                "text_preview": text[:120]
            }
            append_log(record)
            messagebox.showinfo("Saved", f"Audio saved to:\n{out_path}")
            self.status_label.configure(text=f"Saved: {out_path.name}")
        else:
            messagebox.showerror("Error", "Failed to synthesize and save audio.")

    def clear_text(self):
        self.textbox.delete("1.0", "end")
        self.status_label.configure(text="Cleared")

if __name__ == "__main__":
    app = TTSApp()
    app.mainloop()
