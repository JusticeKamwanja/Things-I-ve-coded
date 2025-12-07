from tkinter import StringVar
import customtkinter as ctk
from random import choice
from time import sleep

class App(ctk.CTk):
    def __init__(self):
        '''Initialize the root window ang game attributes.'''
        super().__init__()
        
        # The root window.
        self.title(' ' * 50 + 'Number Guessing Game')
        self.geometry('500x600+450+50')
        self.bgColour = "#11B65B"
        self.config(background=self.bgColour)
        self.resizable(False, False)
        
        # The game attributes.
        self.changingText = StringVar(value='Pick A Number')
        self.maxLimit = 1
        self.attempts = 0
        self.attemptsStatement = StringVar(value=f'Attempts: {self.attempts}')
        self.font = 'Comic Sans MS'
        
        # Run the game
        self.addHomePage()
        
    def pickLevel(self,  level):
        '''This function will decide the levels.
        It picks the level attributes, thenlaunches the game page.'''
        
        if level.lower == 'quick play':
            self.maxLimit = 50
            self.bgColour = "#FFEB33"
            self.config(background=self.bgColour)
            
        if level.lower == 'one':
            self.maxLimit = 100
            self.bgColour = "#33F1FF"
            self.config(background=self.bgColour)

        if level.lower == 'two':
            self.maxLimit = 150
            self.bgColour = "#33FF3D"
            self.config(background=self.bgColour)

        if level.lower == 'three':
            self.maxLimit = 200
            self.bgColour = "#3352FF"
            self.config(background=self.bgColour)

        if level.lower == 'four':
            self.maxLimit = 250
            self.bgColour = "#FF33F5"
            self.config(background=self.bgColour)
        
        self.addGamePage()
        
    # A function to remove widgets.
    def takeAway(self, *widgets):
        for widget in widgets:
            widget.destroy()
        
    # A few functions to handle the pages.
    def addHomePage(self):
        '''A function to load the homepage.'''
        # Reset the random number and the number of attempts.
        self.attempts = 0
        self.randomNumber = choice(range(int(self.maxLimit) + 1))
        
        for widget in self.winfo_children():
            self.takeAway(widget)
        self.addLabel('nUMBER \n' + ' ' * 11 + 'gUESSER', 'Anurati', 60, 0, 0, 2, "#000000", method='grid')
        # The quick play button
        self.addButton('Quick Play', self.pickLevel('quck play'), 0, 1, method='grid')

        # The 'levels' button.
        self.addButton('Levels', self.showLevels, 1, 2, method='grid')
    
    def addGamePage(self):
        '''A function to add the widgets for the gameplay'''
        self.bgColour = "#FCBCBC"
        self.config(background=self.bgColour)
        for widget in self.winfo_children():
            self.takeAway(widget)
        # Adding the neccesary label to the window.
        self.addChangingLabel(self.changingText, 60, "#202109", 50)
        self.addEntryBox()
        self.addChangingLabel(self.attemptsStatement, 30, "#0A4207", 5)
        self.addButton('GUESS', self.guess)
        
    def loadWinningPage(self):
        '''A function to load the winning page.'''
        # Remove the unnecessary widgets for the winning page.
        self.takeAway(self.entry, self.button)
        self.addButton('Play Again', self.addHomePage)
    
    def finalButton(self):
        pass
    
    # A few functions to add the widgets.
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
        
    # The logic.
    def quickPlay(self):
        '''When the user clicks the quick play button.'''
        self.addGamePage()
        
    def showLevels(self):
        '''When the user clicks Play Levels'''
        levels = ['One', 'Two', 'Three', 'Four']
        columns = [0, 1] * 2
        rows = [3, 4, 5, 6]
        
        for level, column, row in zip(levels, columns, rows):
            
            # Add four buttons.
            self.addButton(f'Level {level}', self.pickLevel(f'{level}'), column, row, method='grid')
        
    def guess(self):
        '''Access the content of the entry box.'''
        self.user_entry = self.entry.get()

        # Change the label.
        x = self.user_entry
        if x:
            try:
                x = int(x)
                # Check if the number is correct.
                self.check(self.user_entry)
            except:
                self.changingText.set('Enter a number')
        else:
            return None
            
    def check(self, number):
        '''Give the user some feedback on whether or not the guess is accurate'''
        # Increase the number of attempts by one.
        self.attempts += 1
        a = int(number)
        b = self.randomNumber
        if a > b:
            feedback = 'Too High'
            self.attemptsMessage = f'Attempts: {self.attempts}'
            
        elif a < b:
            feedback = 'Too Low'
            self.attemptsMessage = f'Attempts: {self.attempts}'

        elif a == b:
            # Here the user has won, so we load the winning page.
            self.loadWinningPage()
            feedback = 'YOU WON!!!'
            self.attemptsMessage = (f'Total Attempts: \n{self.attempts}')
            
        self.changingText.set(feedback)
        self.attemptsStatement.set(self.attemptsMessage)

game = App()
game.mainloop()