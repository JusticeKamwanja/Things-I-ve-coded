


# A modern looking dashboard.
from turtle import bgcolor
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Ensuring the main window stays in the middle of the user's screen.
        self.user_screen_width = self.winfo_screenwidth()
        self.user_screen_height = self.winfo_screenheight()
        self.root_window_width = int(self.user_screen_width * 0.9)
        self.root_window_height = int(self.user_screen_height * 0.8)

        # Center the window on the screen (x,y offsets)
        x_offset = int((self.user_screen_width - self.root_window_width) / 2)
        y_offset = int((self.user_screen_height - self.root_window_height) / 2)
        
        # Initializing the main window.
        self.title('Modern Looking Dashboard')
        self.geometry(f'{self.root_window_width}x{self.root_window_height}+{x_offset}+{y_offset}')
        # self.config(background="#1A1919")
        self._set_appearance_mode("dark")
        self.config(background='black')
        
        # This will dictate the width of the sidebar and the rest of the window.
        self.percentage_of_total_width = 0.2 #(20%)
        
        # Build the Dashboard
        self.build_dashboard()
        
    def build_dashboard(self):
        self.add_frames()
        
    def add_frames(self):
        # This will add all the necessary frames.
        self.add_sidebar_frame()
        self.add_main_window()
        
    def add_sidebar_frame(self):
        # This will add a sidebar to the left of the dashboard.
        self.sidebar_width = int(self.root_window_width * self.percentage_of_total_width)
        self.sidebar = ctk.CTkFrame(self, height=self.root_window_height, width=self.sidebar_width, fg_color=("#496F9B", "#141414"))
        self.sidebar.pack(side='left')
        self.sidebar.pack_propagate(False)
        
    def add_main_window(self):
        self.main_window_width = int(self.root_window_width * (1 - self.percentage_of_total_width))
        self.main_window = ctk.CTkScrollableFrame(self, fg_color=("#5B8BC2", "#070707"))
        self.main_window.pack(side='right', fill='both', expand=True, pady=30, padx=30)
        self.main_window.pack_propagate(False)
        
app = App()
if __name__ == "__main__":
    app.mainloop()