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
        
        # Initial call to render any existing tasks (e.g., if loading from a file)
        # For this example, we start empty.
        self.render_tasks()

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
        
    def delete_task(self, index):
        """Deletes a task by its index and re-renders."""
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.render_tasks()
            
    def toggle_complete(self, index):
        """Toggles the completion status of a task."""
        if 0 <= index < len(self.tasks):
            # Toggle status: 0 to 1, or 1 to 0
            self.tasks[index][1] = 1 - self.tasks[index][1] 
            self.render_tasks()

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