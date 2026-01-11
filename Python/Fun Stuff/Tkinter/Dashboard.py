import customtkinter as ctk
import random
import time

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # 1. Screen Dimension Logic
        self.user_screen_width = self.winfo_screenwidth()
        self.user_screen_height = self.winfo_screenheight()
        self.root_window_width = int(self.user_screen_width * 0.9)
        self.root_window_height = int(self.user_screen_height * 0.8)

        # Center calculation
        x_offset = int((self.user_screen_width - self.root_window_width) / 2)
        y_offset = int((self.user_screen_height - self.root_window_height) / 2)
        
        # 2. Window Configuration
        self.title('Modern Looking Dashboard')
        self.geometry(f'{self.root_window_width}x{self.root_window_height}+{x_offset}+{y_offset}')
        self._set_appearance_mode("light")
        self.configure(fg_color=("#000000", '#80EDF5')) # Main app background
        
        # 3. Layout Grid Configuration
        # Column 0 is the Sidebar (Fixed width), Column 1 is the Main Area (Expands)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.percentage_of_total_width = 0.2
        self.sidebar_width = int(self.root_window_width * self.percentage_of_total_width)
        self.main_window_width = 1 - self.sidebar_width
        self.number_of_columns = 3
        
        self.build_dashboard()
        
    def build_dashboard(self):
        # We call the frame creators in order
        self.add_sidebar()
        self.add_main_window()
        self.add_top_window()
        self.add_other_windows()
        
    def add_sidebar(self):
        # Kept your colors: Light Blue-Grey for Light Mode, Deep Grey for Dark Mode
        self.sidebar = ctk.CTkFrame(
            self, 
            width=self.sidebar_width, 
            corner_radius=0,
            fg_color=("#537DAD", "#6B6767")
        )
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        # Prevents the sidebar from shrinking to fit its contents
        self.sidebar.grid_propagate(False)
        
    def add_main_window(self):
        self.main_window = ctk.CTkScrollableFrame(
            self, 
            fg_color=("#5B8BC2", "#6D6565"), 
            bg_color="#070707", # Border/Background color
            corner_radius=15
        )
        # Keep a 20px margin around the main area so right column stops 20px
        self.main_window.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # Inside the scrollable frame configure two logical columns:
        # - column 0: fixed/compact column (left cards)
        # - column 1: expanding column that stretches to the right (right cards)
        try:
            # CTkScrollableFrame exposes grid methods similar to a normal frame
            self.main_window.grid_columnconfigure(0, weight=0)
            self.main_window.grid_columnconfigure(1, weight=1)
        except Exception:
            pass
        
    def add_top_window(self):
        top_height = int(self.root_window_height * 0.3)

        self.top_window = ctk.CTkFrame(
            self.main_window,
            height=top_height,
            fg_color=("#649DCC", "#141414"),
            )
        
        # Using pack inside the scrollable frame is fine as it ensures vertical stacking
        self.top_window.grid(
            columnspan=self.number_of_columns,
            padx=10,
            pady=10,
            sticky='ew'
            )

        # Make the top window stretch horizontally across both logical columns
        try:
            self.main_window.grid_columnconfigure(0, minsize=300)
        except Exception:
            pass

        
    def add_other_windows(self):
        # Create reusable info cards and populate left (column 0) and right (column 1)
        self.info_cards = []

        def create_info_card(parent, row, column, title):
            card = ctk.CTkFrame(parent, fg_color="#2B2626", corner_radius=10)
            card.grid(row=row, column=column, padx=10, pady=10, sticky='nsew')

            # Title label
            title_lbl = ctk.CTkLabel(card, text=title, anchor='w', font=ctk.CTkFont(size=14, weight='bold'))
            title_lbl.grid(row=0, column=0, sticky='ew', padx=12, pady=(12, 4))

            # Dynamic value label
            value_lbl = ctk.CTkLabel(card, text='—', anchor='w', font=ctk.CTkFont(size=22))
            value_lbl.grid(row=1, column=0, sticky='ew', padx=12, pady=(0, 12))

            # Allow the card content to stretch
            card.grid_columnconfigure(0, weight=1)

            self.info_cards.append((card, title_lbl, value_lbl))
            return card

        # Left column: compact list (fixed width-ish)
        left_rows = 2
        for i in range(left_rows):
            create_info_card(self.main_window, row=i + 1, column=0, title=f'Left Card {i+1}')

        # Right column: expanding; will take remaining horizontal space up to the 20px outer margin
        right_rows = 4
        for i in range(right_rows):
            create_info_card(self.main_window, row=i + 1, column=1, title=f'Right Card {i+1}')

        # Ensure the right column expands and its children stretch horizontally
        try:
            self.main_window.grid_columnconfigure(1, weight=1)
        except Exception:
            pass

        # Start periodic updates for the values
        self.after(500, self.update_info_cards)

    def update_info_cards(self):
        # Update the value label of each card with lightweight random info
        for _, title_lbl, value_lbl in self.info_cards:
            # Example random contents: percent, integer, or short text
            t = random.choice(['percent', 'int', 'text'])
            if t == 'percent':
                value = f"{random.randint(0,100)}%"
            elif t == 'int':
                value = str(random.randint(0, 10_000))
            else:
                value = random.choice(['OK', 'WARN', 'ERR', 'IDLE'])
            value_lbl.configure(text=value)

        # schedule next update (efficient, non-blocking)
        self.after(2000, self.update_info_cards)

if __name__ == "__main__":
    app = App()
    app.mainloop()