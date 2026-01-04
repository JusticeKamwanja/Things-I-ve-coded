# A modern looking dashboard.
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Initializing the main window.
        # Ensuring the main window stays in the middle of the user's screen.
        user_screen_width = self.winfo_screenwidth()
        user_screen_height = self.winfo_screenheight()
        root_window_width = int(user_screen_width * 0.9)
        root_window_height = int(user_screen_height * 0.8)

        # Center the window on the screen (x,y offsets)
        x_offset = int((user_screen_width - root_window_width) / 2)
        y_offset = int((user_screen_height - root_window_height) / 2)
        
        self.title('Modern Looking Dashboard')
        self.geometry(f'{root_window_width}x{root_window_height}+{x_offset}+{y_offset}')
        
        def addWidgets(self):
            pass
            
        def add_sidebar_frame(self):
            # This will add a sidebar to the left of the dashboard.
        
app = App()
if __name__ == "__main__":
    app.mainloop()