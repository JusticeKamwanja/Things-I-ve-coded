import os
import json
import base64
import ctypes
import sys
import customtkinter as ctk
from tkinter import StringVar, W, E

class ToDoApp(ctk.CTk):
    """A simple To-Do List application with a CustomTkinter GUI."""
    
    def __init__(self):
        super().__init__()

        # --- Root Window Setup ---
        self.title("CustomTkinter To-Do List")
        self.geometry("500x700")
        self.resizable(False, False)
        
        # Set theme and color scheme
        ctk.set_appearance_mode("System")  # Options: "Light", "Dark", "System"
        ctk.set_default_color_theme("blue") # Options: "blue", "green", "dark-blue"

        # List to store the tasks (strings)
        self.tasks = []
        
        # Configure grid for the main window (1 row, 1 column)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0) # Header section
        self.grid_rowconfigure(1, weight=1) # Scrollable frame section

        # --- Build the GUI Components ---
        self.create_header()
        self.create_scrollable_task_list()
        
        # Setup storage, load any existing tasks, and render
        self.setup_storage()
        self.load_tasks()
        self.render_tasks()

        # Ensure tasks are saved when the window closes
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    # ====================================================================
    # 1. UI SETUP METHODS
    # ====================================================================

    def create_header(self):
        """Creates the header frame for input and adding tasks."""
        
        header_frame = ctk.CTkFrame(self)
        header_frame.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")
        
        # Configure grid for the header frame (1 row, 3 columns)
        header_frame.grid_columnconfigure(0, weight=4)
        header_frame.grid_columnconfigure(1, weight=1)

        # 1. Task Input Entry
        self.task_input = ctk.CTkEntry(
            header_frame, 
            placeholder_text="Enter new task...",
            font=("Arial", 16)
        )
        self.task_input.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="ew")
        
        # Bind the Enter key to the add_task method
        self.task_input.bind("<Return>", lambda event: self.add_task())

        # 2. Add Button
        add_button = ctk.CTkButton(
            header_frame, 
            text="Add", 
            command=self.add_task
        )
        add_button.grid(row=0, column=1, padx=(5, 10), pady=10, sticky="e")
        
    def create_scrollable_task_list(self):
        """Creates the scrollable frame that will hold the individual tasks."""
        
        self.scrollable_frame = ctk.CTkScrollableFrame(self, label_text="Tasks Pending", fg_color="transparent")
        self.scrollable_frame.grid(row=1, column=0, padx=20, pady=(10, 20), sticky="nsew")
        
        # Configure grid for the scrollable frame (only one column is needed)
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

    # ====================================================================
    # 2. DATA AND RENDERING METHODS
    # ====================================================================

    def add_task(self):
        """Adds a new task from the input field to the list and re-renders."""
        
        task_text = self.task_input.get().strip()
        
        if task_text:
            # Task format: (task_text, status: 0=pending, 1=complete)
            self.tasks.append([task_text, 0])
            self.task_input.delete(0, 'end') # Clear input field
            self.render_tasks()
            self.save_tasks()
        
    def delete_task(self, index):
        """Deletes a task by its index and re-renders."""
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.render_tasks()
            self.save_tasks()
            
    def toggle_complete(self, index):
        """When a task is marked complete, remove it and save immediately."""
        if 0 <= index < len(self.tasks):
            # Delete the task when it's marked complete
            del self.tasks[index]
            self.render_tasks()
            self.save_tasks()

    # ====================================================================
    # 3. PERSISTENCE & WINDOWS-HIDDEN STORAGE
    # ====================================================================

    def setup_storage(self):
        """Prepare storage directory and file path in %APPDATA% (Windows-optimized)."""
        appdata = os.getenv('APPDATA') or os.path.expanduser('~')
        storage_dir = os.path.join(appdata, 'Microsoft', 'Windows', 'CTK_Todo')
        try:
            os.makedirs(storage_dir, exist_ok=True)
        except Exception:
            storage_dir = os.path.join(appdata, 'CTK_Todo')
            os.makedirs(storage_dir, exist_ok=True)

        # Use a less-obvious filename; we'll set hidden+system attributes on Windows
        self._data_file = os.path.join(storage_dir, 'data.bin')

        # If running on Windows, set hidden attributes for the folder and file
        if sys.platform.startswith('win'):
            try:
                FILE_ATTRIBUTE_HIDDEN = 0x02
                FILE_ATTRIBUTE_SYSTEM = 0x04
                attrs = FILE_ATTRIBUTE_HIDDEN | FILE_ATTRIBUTE_SYSTEM
                ctypes.windll.kernel32.SetFileAttributesW(storage_dir, attrs)
            except Exception:
                # fallback to attrib command
                try:
                    os.system(f'attrib +h +s "{storage_dir}"')
                except Exception:
                    pass

    def set_file_hidden(self, path):
        """Set Windows hidden/system attributes on a file. Silent on failure."""
        if not sys.platform.startswith('win'):
            return
        try:
            FILE_ATTRIBUTE_HIDDEN = 0x02
            FILE_ATTRIBUTE_SYSTEM = 0x04
            attrs = FILE_ATTRIBUTE_HIDDEN | FILE_ATTRIBUTE_SYSTEM
            ctypes.windll.kernel32.SetFileAttributesW(path, attrs)
        except Exception:
            try:
                os.system(f'attrib +h +s "{path}"')
            except Exception:
                pass

    def save_tasks(self):
        """Save tasks to the hidden data file using base64-encoded JSON."""
        try:
            data = json.dumps(self.tasks, ensure_ascii=False)
            encoded = base64.b64encode(data.encode('utf-8'))
            with open(self._data_file, 'wb') as f:
                f.write(encoded)
            # Ensure the file is hidden on Windows
            self.set_file_hidden(self._data_file)
        except Exception as e:
            print('Save failed:', e)

    def load_tasks(self):
        """Load tasks from the hidden data file if it exists."""
        try:
            if not os.path.exists(self._data_file):
                return
            with open(self._data_file, 'rb') as f:
                encoded = f.read()
            if not encoded:
                return
            try:
                decoded = base64.b64decode(encoded).decode('utf-8')
                self.tasks = json.loads(decoded)
            except Exception:
                # If decode fails, attempt to load as plain JSON text
                try:
                    self.tasks = json.loads(encoded.decode('utf-8'))
                except Exception:
                    self.tasks = []
        except Exception as e:
            print('Load failed:', e)

    def on_close(self):
        """Save tasks and close the app."""
        try:
            self.save_tasks()
        finally:
            self.destroy()

    def render_tasks(self):
        """Clears the scrollable frame and recreates all task widgets based on self.tasks list."""
        
        # Destroy all existing widgets in the scrollable frame
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Re-render tasks
        for index, (task_text, status) in enumerate(self.tasks):
            # Create a dedicated frame for each task entry
            task_frame = ctk.CTkFrame(self.scrollable_frame, fg_color="transparent")
            task_frame.grid(row=index, column=0, padx=10, pady=5, sticky="ew")
            
            # Configure grid for the task frame (Checkbox:1, Label:4, DeleteButton:1)
            task_frame.grid_columnconfigure(0, weight=1) # Checkbox
            task_frame.grid_columnconfigure(1, weight=6) # Task Text
            task_frame.grid_columnconfigure(2, weight=1) # Delete Button

            # 1. Checkbox for completion status
            check_var = StringVar(value="on" if status == 1 else "off")
            checkbox = ctk.CTkCheckBox(
                task_frame, 
                text="", 
                variable=check_var, 
                onvalue="on", 
                offvalue="off",
                command=lambda i=index: self.toggle_complete(i)
            )
            checkbox.grid(row=0, column=0, padx=(0, 10), sticky=W)
            
            # 2. Task Label
            task_label = ctk.CTkLabel(
                task_frame, 
                text=task_text, 
                font=("Arial", 16),
                anchor="w" # Anchor west (left)
            )
            task_label.grid(row=0, column=1, sticky="ew")
            
            # Apply strikethrough effect if complete
            if status == 1:
                # Note: CustomTkinter labels don't natively support strikethrough.
                # A common Tkinter trick is to manually reconfigure the font,
                # but a simpler CTk-friendly solution is often to use a different color.
                task_label.configure(text_color="#888888") 
            
            # 3. Delete Button
            delete_button = ctk.CTkButton(
                task_frame, 
                text="X", 
                width=30, 
                height=30, 
                fg_color="red", 
                hover_color="#CC0000",
                command=lambda i=index: self.delete_task(i)
            )
            delete_button.grid(row=0, column=2, sticky=E)
            
# --- Application Launch ---
if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()