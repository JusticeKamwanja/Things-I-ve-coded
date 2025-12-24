from tkinter import StringVar
import customtkinter as ctk
from random import choice

class App(ctk.CTk):
    def __init__(self):
        '''Initialize the root window and game attributes.'''
        super().__init__()

        # The root window.
        self.title(' ' * 50 + 'Number Guessing Game')
        self.geometry('500x600+450+50')
        self.bgColour = "#11B65B"
        self.config(background=self.bgColour)
        self.resizable(False, False)

        # Game attributes.
        self.changingText = StringVar(value='Pick A Number')
        self.maxLimit = 1
        self.attempts = 0
        self.attemptsStatement = StringVar(value=f'Attempts: {self.attempts}')
        self.font = 'Comic Sans MS'

        # Run the game
        self.addHomePage()

    def addHomePage(self):
        '''Load the homepage.'''
        self.attempts = 0
        self.changingText.set('Pick A Number')  # Reset the changing text
        self.randomNumber = choice(range(self.maxLimit + 1))
        
        for widget in self.winfo_children():
            self.takeAway(widget)
        self.addLabel('nUMBER \n' + ' ' * 11 + 'gUESSER', 'Anurati', 60, 0, 0, 2, "#000000", method='pack')
        
        # Correct lambda usage for button commands
        self.addButton('Quick Play', lambda: self.pickLevel(50), 0, 1, method='pack')
        self.addButton('Levels', self.showLevels, 1, 2, method='pack')

    def showLevels(self):
        '''When the user clicks Play Levels.'''
        # Clear the current widgets
        for widget in self.winfo_children():
            self.takeAway(widget)

        # Define levels and their limits
        levels = [
            ('Quick Play', 50),
            ('Level One', 100),
            ('Level Two', 150),
            ('Level Three', 200),
            ('Level Four', 250)
        ]
        
        # Add buttons for each level
        for index, (label, limit) in enumerate(levels):
            self.addButton(label, lambda l=limit: self.pickLevel(l), 0, index, method='grid')

    def pickLevel(self, level):
        '''Decide the level attributes and launch the game page.'''
        self.maxLimit = level  # Set maxLimit directly to the provided level
        self.randomNumber = choice(range(self.maxLimit + 1))  # Generate the random number after setting maxLimit
        self.addGamePage()

    def takeAway(self, *widgets):
        for widget in widgets:
            widget.destroy()

    def addGamePage(self):
        '''Add the widgets for gameplay.'''
        self.bgColour = "#FCBCBC"
        self.config(background=self.bgColour)
        for widget in self.winfo_children():
            self.takeAway(widget)
        self.addChangingLabel(self.changingText, 60, "#202109", 50)
        self.addEntryBox()
        self.addChangingLabel(self.attemptsStatement, 30, "#0A4207", 5)
        self.addButton('GUESS', self.guess)

    def loadWinningPage(self):
        '''Load the winning page.'''
        self.takeAway(self.entry, self.button)
        self.addButton('Play Again', self.addHomePage)

    def addLabel(self, text, font_type, font_size, column=0, row=0, columnspan=0, colour='white', method='pack'):
        self.changingLabel = ctk.CTkLabel(self, text=text, font=(font_type, font_size), bg_color=self.bgColour, text_color=colour)
        if method == 'pack':
            self.changingLabel.pack(pady=20)
        elif method == 'grid':
            self.changingLabel.grid(column=column, row=row, columnspan=columnspan, pady=10)

    def addButton(self, message, command, column=0, row=0, method='pack'):
        self.button = ctk.CTkButton(self, text=message, font=('Bauhaus 93', 30), command=command, bg_color=self.bgColour)
        if method == 'pack':
            self.button.pack(pady=20)
        elif method == 'grid':
            self.button.grid(column=column, row=row, pady=10)

    def addEntryBox(self):
        self.entry = ctk.CTkEntry(self, width=300, height=60, font=(self.font, 40), bg_color='transparent', fg_color="#E988C7", text_color='#000000')
        self.entry.pack(pady=20)

    def addChangingLabel(self, textvariable, font_size, text_color, pad_value):
        self.label = ctk.CTkLabel(self, textvariable=textvariable, font=(self.font, font_size), bg_color=self.bgColour, text_color=text_color)
        self.label.pack(pady=pad_value)

    def guess(self):
        '''Access the content of the entry box.'''
        self.user_entry = self.entry.get()

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
        
        if number > self.randomNumber:
            feedback = 'Too High'
        elif number < self.randomNumber:
            feedback = 'Too Low'
        else:
            feedback = 'YOU WON!!!'
            self.attemptsStatement.set(f'Total Attempts: {self.attempts}')
            self.loadWinningPage()

        self.changingText.set(feedback)
        self.attemptsStatement.set(f'Attempts: {self.attempts}')

game = App()
game.mainloop()