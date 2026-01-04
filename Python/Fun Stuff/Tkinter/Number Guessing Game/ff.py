from tkinter import StringVar, font
import customtkinter as ctk
from random import choice

class App(ctk.CTk):
    def __init__(self):
        '''Initialize the root window and game attributes.'''
        super().__init__()

        # --- Root Window Setup ---
        self.title(' ' * 50 + 'Number Guessing Game')
        self.geometry('1200x600+80+50')
        self.initial_bg_colour = "#11B65B" # Defined a consistent initial colour
        self.config(background=self.initial_bg_colour)
        self.resizable(False, False)

        # --- Game Attributes ---
        self.changingText = StringVar(value='Pick A Number')
        self.maxLimit = 1
        self.attempts = 0
        self.attemptsStatement = StringVar(value=f'Attempts: {self.attempts}')
        self.font = 'Comic Sans MS' # Using a consistent default font

        # --- Run the game ---
        self.addHomePage()

    # =========================
    # VIEW MANAGEMENT
    # =========================

    def takeAway(self):
        '''Destroys all child widgets of the root window.'''
        for widget in self.winfo_children():
            widget.destroy()

    def addHomePage(self):
        '''Load the homepage.'''
        
        # Reset game state and view
        self.takeAway()
        self.config(background=self.initial_bg_colour)
        self.attempts = 0
        self.changingText.set('Pick A Number')

        # Home Page Widgets
        self.addLabel('\nnUMBER \n' + ' ' * 11 + 'gUESSER', 'Anurati', 60, colour="#000000", method='pack')
        
        # Use pack for simplicity on homepage
        self.addButton('Quick Play (0-50)', lambda: self.pickLevel(50), method='pack')
        self.addButton('Select Level', self.showLevels, method='pack')

    def showLevels(self):
        '''When the user clicks Select Levels.'''
        self.takeAway()

        # Define levels and their limits
        levels = [
            ('Level 1 (0-100)', 100),
            ('Level 2 (0-150)', 150),
            ('Level 3 (0-200)', 200),
            ('Level 4 (0-250)', 250),
            ('Back', self.addHomePage)
        ]
        
        # Use grid for structured layout
        for index, (label, limit) in enumerate(levels):
            if label == 'Back':
                self.addButton(label, limit, 0, index + 1, method='pack') # 'limit' is the function here
            
            # For the level buttons.
            else:
                self.addButton(label, lambda l=limit: self.pickLevel(l), 0, index, method='pack')

    def pickLevel(self, level):
        '''Decide the level attributes and launch the game page.'''
        self.maxLimit = level  # Set maxLimit
        self.randomNumber = choice(range(self.maxLimit + 1))  # Generate the random number .
        self.addGamePage()

    def addGamePage(self):
        '''Add the widgets for gameplay.'''
        self.takeAway()
        self.game_bg_colour = "#FCBCBC" # Defined a consistent game colour
        self.config(background=self.game_bg_colour)
        
        self.addChangingLabel(self.changingText, 30, "#202109", 50)
        self.addEntryBox()
        self.addChangingLabel(self.attemptsStatement, 30, "#0A4207", 5)
        # Store guess button and entry box to easily destroy them later
        self.guess_button = self.addButton('GUESS', self.guess) 
        self.entry.focus_set() # Set focus to the entry box immediately

    def loadWinningPage(self):
        '''Load the winning page.'''
        # Destroy the entry and guess button stored as attributes
        self.entry.destroy()
        self.guess_button.destroy()
        
        # Add a new Play Again button
        self.addButton('Play Again', self.addHomePage)

    # =========================
    # WIDGET CREATION HELPERS
    # =========================

    def addLabel(self, text, font_type, font_size, column=0, row=0, columnspan=0, colour='white', method='pack'):
        label = ctk.CTkLabel(self, text=text, font=(font_type, font_size), bg_color=self.cget("background"), text_color=colour)
        if method == 'pack':
            label.pack(pady=20)
        elif method == 'grid':
            label.grid(column=column, row=row, columnspan=columnspan, pady=10)
        return label

    def addButton(self, message, command, column=0, row=0, method='pack'):
        button = ctk.CTkButton(self, text=message, font=('Bauhaus 93', 30), command=command, bg_color=self.cget("background"))
        if method == 'pack':
            button.pack(pady=20)
        elif method == 'grid':
            button.grid(column=column, row=row, pady=10)
        return button # Return the created button object

    def addEntryBox(self):
        # Stored as attribute because it needs to be accessed for self.entry.get() and destruction
        self.entry = ctk.CTkEntry(self, width=300, height=60, font=(self.font, 30), bg_color='transparent', fg_color="#E988C7", text_color='#000000')
        self.entry.pack(pady=20)
        # Add binding to allow pressing Enter to submit
        self.entry.bind('<Return>', lambda event: self.guess()) 

    def addChangingLabel(self, textvariable, font_size, text_color, pad_value):
        label = ctk.CTkLabel(self, textvariable=textvariable, font=(self.font, font_size), bg_color=self.cget("background"), text_color=text_color)
        label.pack(pady=pad_value)
        return label

    # =========================
    # GAME LOGIC
    # =========================

    def guess(self, event=None): # Added event=None to handle the bind call
        '''Access the content of the entry box and validate.'''
        self.user_entry = self.entry.get()
        self.entry.delete(0, 'end') # Clear the entry box after guessing

        if self.user_entry:
            try:
                x = int(self.user_entry)
                self.check(x)
            except ValueError:
                self.changingText.set('Enter a valid number')
        else:
            self.changingText.set('Please enter a number')

    def check(self, number):
        '''Give feedback on the guess.'''
        self.attempts += 1
        feedback = ''
        
        # Check if the guess is within the limit (good user feedback)
        if number < 0 or number > self.maxLimit:
            feedback = f'Pick from 0 - {self.maxLimit}'
        elif number > self.randomNumber:
            feedback = 'Too High'
        elif number < self.randomNumber:
            feedback = 'Too Low'
        else:
            feedback = f'YOU WON!!! \nYou took {self.attempts} attempts.'
            self.changingText.set(feedback)
            self.attemptsStatement.set('')
            self.loadWinningPage()
            return # Exit function after win

        self.changingText.set(feedback)
        self.attemptsStatement.set(f'Attempts: {self.attempts}')

# --- Application Launch ---
if __name__ == "__main__":
    game = App()
    game.mainloop()