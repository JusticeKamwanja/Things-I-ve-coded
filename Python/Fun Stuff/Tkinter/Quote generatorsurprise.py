import customtkinter as ctk
import json
import csv
import random
import datetime
import os
from pathlib import Path

# Configure appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class QuoteMoodApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("✨ Quote Mood Journal")
        self.geometry("900x700")
        self.resizable(False, False)
        
        # Create data directory
        self.data_dir = Path("journal_data")
        self.data_dir.mkdir(exist_ok=True)
        self.quotes_file = self.data_dir / "quotes.txt"
        self.entries_file = self.data_dir / "entries.json"
        
        # Initialize data
        self.init_quotes_file()
        self.load_entries()
        
        # Main container
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        title = ctk.CTkLabel(
            main_frame,
            text="✨ Daily Quote & Mood Journal",
            font=("Helvetica", 24, "bold")
        )
        title.pack(pady=(0, 20))
        
        # Quote section
        self.create_quote_section(main_frame)
        
        # Journal section
        self.create_journal_section(main_frame)
        
        # Export section
        export_frame = ctk.CTkFrame(main_frame)
        export_frame.pack(fill="x", pady=(20, 0))
        
        export_btn = ctk.CTkButton(
            export_frame,
            text="📊 Export to CSV",
            command=self.export_to_csv,
            fg_color="#4CAF50",
            hover_color="#45a049"
        )
        export_btn.pack(side="left", padx=(0, 10))
        
        clear_btn = ctk.CTkButton(
            export_frame,
            text="🗑️ Clear All Data",
            command=self.clear_data,
            fg_color="#f44336",
            hover_color="#da190b"
        )
        clear_btn.pack(side="left")
        
        stats_label = ctk.CTkLabel(
            export_frame,
            text=f"Total Entries: {len(self.entries)}",
            font=("Helvetica", 12)
        )
        stats_label.pack(side="right")
        self.stats_label = stats_label
    
    def create_quote_section(self, parent):
        quote_frame = ctk.CTkFrame(parent, fg_color="#1a1a1a", corner_radius=10)
        quote_frame.pack(fill="x", pady=(0, 20))
        
        # Quote display
        self.quote_label = ctk.CTkLabel(
            quote_frame,
            text="Click 'Get Quote' to start",
            font=("Helvetica", 14),
            wraplength=800,
            text_color="#E0E0E0"
        )
        self.quote_label.pack(padx=20, pady=(20, 10))
        
        # Mood indicator
        mood_frame = ctk.CTkFrame(quote_frame, fg_color="transparent")
        mood_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        mood_label = ctk.CTkLabel(mood_frame, text="Mood:", font=("Helvetica", 12))
        mood_label.pack(side="left", padx=(0, 10))
        
        self.mood_label = ctk.CTkLabel(
            mood_frame,
            text="Neutral",
            font=("Helvetica", 12, "bold"),
            text_color="#FFD700"
        )
        self.mood_label.pack(side="left")
        
        # Button
        get_quote_btn = ctk.CTkButton(
            quote_frame,
            text="🎲 Get Random Quote",
            command=self.get_random_quote,
            font=("Helvetica", 12),
            height=40
        )
        get_quote_btn.pack(pady=(0, 20), padx=20, fill="x")
    
    def create_journal_section(self, parent):
        journal_frame = ctk.CTkFrame(parent, fg_color="#1a1a1a", corner_radius=10)
        journal_frame.pack(fill="both", expand=True, pady=(0, 20))
        
        journal_title = ctk.CTkLabel(
            journal_frame,
            text="📝 Your Thoughts",
            font=("Helvetica", 16, "bold")
        )
        journal_title.pack(padx=20, pady=(20, 10), anchor="w")
        
        # Text input
        self.journal_text = ctk.CTkTextbox(
            journal_frame,
            height=200,
            fg_color="#2a2a2a",
            text_color="#E0E0E0",
            font=("Helvetica", 11)
        )
        self.journal_text.pack(fill="both", expand=True, padx=20, pady=(0, 15))
        
        # Save button
        save_btn = ctk.CTkButton(
            journal_frame,
            text="💾 Save Entry",
            command=self.save_entry,
            font=("Helvetica", 12),
            height=35
        )
        save_btn.pack(pady=(0, 20), padx=20, fill="x")
    
    def init_quotes_file(self):
        """Initialize quotes file with sample quotes"""
        if not self.quotes_file.exists():
            quotes = [
                "The only way to do great work is to love what you do. - Steve Jobs",
                "Innovation distinguishes between a leader and a follower. - Steve Jobs",
                "Life is what happens when you're busy making other plans. - John Lennon",
                "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
                "It is during our darkest moments that we must focus to see the light. - Aristotle",
                "The only impossible journey is the one you never begin. - Tony Robbins",
                "In the middle of difficulty lies opportunity. - Albert Einstein",
                "Success is not final, failure is not fatal. - Winston Churchill",
                "Believe you can and you're halfway there. - Theodore Roosevelt",
                "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
                "You miss 100% of the shots you don't take. - Wayne Gretzky",
                "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
                "Everything you want is on the other side of fear. - Jack Canfield",
                "Do not watch the clock; do what it does. Keep going. - Sam Levenson",
                "The best revenge is massive success. - Frank Sinatra"
            ]
            with open(self.quotes_file, 'w') as f:
                f.write('\n'.join(quotes))
    
    def get_random_quote(self):
        """Load and display a random quote with mood analysis"""
        with open(self.quotes_file, 'r') as f:
            quotes = [line.strip() for line in f.readlines() if line.strip()]
        
        quote = random.choice(quotes)
        self.quote_label.configure(text=quote)
        
        # Analyze mood based on keywords
        mood = self.analyze_mood(quote.lower())
        self.mood_label.configure(text=mood["label"])
        self.mood_label.configure(text_color=mood["color"])
    
    def analyze_mood(self, text):
        """Simple sentiment analysis based on keywords"""
        positive = ["love", "success", "great", "best", "beautiful", "dream", "future", "achieve"]
        negative = ["impossible", "failure", "fear", "dark", "doubt"]
        
        pos_count = sum(1 for word in positive if word in text)
        neg_count = sum(1 for word in negative if word in text)
        
        if pos_count > neg_count:
            return {"label": "😊 Inspiring", "color": "#4CAF50"}
        elif neg_count > pos_count:
            return {"label": "🤔 Reflective", "color": "#FF9800"}
        else:
            return {"label": "😌 Neutral", "color": "#FFD700"}
    
    def save_entry(self):
        """Save journal entry with timestamp"""
        text = self.journal_text.get("1.0", "end").strip()
        
        if not text:
            self.show_message("⚠️ Please write something first!")
            return
        
        quote = self.quote_label.cget("text")
        entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "text": text,
            "quote": quote,
            "mood": self.mood_label.cget("text")
        }
        
        self.entries.append(entry)
        with open(self.entries_file, 'w') as f:
            json.dump(self.entries, f, indent=2)
        
        self.journal_text.delete("1.0", "end")
        self.stats_label.configure(text=f"Total Entries: {len(self.entries)}")
        self.show_message("✅ Entry saved successfully!")
    
    def load_entries(self):
        """Load existing entries from JSON"""
        if self.entries_file.exists():
            with open(self.entries_file, 'r') as f:
                self.entries = json.load(f)
        else:
            self.entries = []
    
    def export_to_csv(self):
        """Export all entries to CSV"""
        if not self.entries:
            self.show_message("⚠️ No entries to export!")
            return
        
        csv_file = self.data_dir / f"journal_export_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "Mood", "Entry Text", "Quote"])
            
            for entry in self.entries:
                writer.writerow([
                    entry["timestamp"],
                    entry["mood"],
                    entry["text"][:50] + "..." if len(entry["text"]) > 50 else entry["text"],
                    entry["quote"][:50] + "..." if len(entry["quote"]) > 50 else entry["quote"]
                ])
        
        self.show_message(f"✅ Exported to {csv_file.name}")
    
    def clear_data(self):
        """Clear all journal entries"""
        self.entries.clear()
        with open(self.entries_file, 'w') as f:
            json.dump([], f)
        self.stats_label.configure(text="Total Entries: 0")
        self.show_message("🗑️ All data cleared")
    
    def show_message(self, msg):
        """Show temporary message"""
        popup = ctk.CTkToplevel(self)
        popup.title("Message")
        popup.geometry("300x100")
        popup.after(1500, popup.destroy)
        
        label = ctk.CTkLabel(popup, text=msg, font=("Helvetica", 12))
        label.pack(expand=True)

if __name__ == "__main__":
    app = QuoteMoodApp()
    app.mainloop()
