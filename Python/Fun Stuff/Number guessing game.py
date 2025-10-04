from tkinter import StringVar
import customtkinter as ctk
from random import choice


class App(ctk.CTk):
    def __init__(self):
        '''Initialize the root window ang game attributes.'''
        super().__init__()
        
        # The root window.
        self.title('Number Guessing Game')
        self.geometry('500x600+450+50')
        self.bgColour = "#FCBCBC"
        self.config(background=self.bgColour)
        
        # The game attributes.
        self.changingText = StringVar(value='Pick A Number')
        # self.randomNumber = choice(range(101))
        self.randomNumber = 50
        self.attempts = 0
        self.attemptsStatement = StringVar(value=f'Attempts: {self.attempts}')
        self.font = 'Comic Sans MS'
        
        self.addGamePage()
        
    # A function to remove widgets.
    def takeAway(self, *widgets):
        for widget in widgets:
            widget.destroy()
        
    # A few functions to handle the pages.
    def addHomePage(self):
        '''A function to load the homepage.'''
    
    def addGamePage(self):
        '''A function to add the widgets for the gameplay'''
        # Adding the neccesary label to the window.
        self.addChangingLabel(self.changingText, 60, "#202109", 50)
        self.addEntryBox()
        self.addChangingLabel(self.attemptsStatement, 30, "#0A4207", 5)
        self.addButton()
        
    def loadWinningPage(self):
        '''A function to load the winning page.'''
        self.takeAway(self.entry, self.button)
    
    # A few functions to add the widgets.
    def addLabel(self, text, colour='white'):
        self.changingLabel = ctk.CTkLabel(self, text=text, font=(self.font, 40), bg_color=self.bgColour, text_color=colour)
        self.changingLabel.pack(pady=20)
        
    def addEntryBox(self):
        self.entry = ctk.CTkEntry(self, width=300, height=60, font=(self.font, 40), bg_color='transparent', fg_color="#E988C7", text_color='#000000')
        self.entry.pack(pady=20)
        
    def addChangingLabel(self, textvariable, font_size, text_color, pad_value):
        self.label = ctk.CTkLabel(self, textvariable=textvariable, font=(self.font, font_size), bg_color=self.bgColour, text_color=text_color)
        self.label.pack(pady=pad_value)
        
    def addButton(self):
        self.button = ctk.CTkButton(self, text='GUESS', font=('Bauhaus 93', 30), command=self.guess, bg_color=self.bgColour)
        self.button.pack(pady=20)
        
    # The logic.
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
        number = int(number)
        if number > self.randomNumber:
            feedback = 'Too High'
            self.attemptsMessage = f'Attempts: {self.attempts}'
            
        elif number < self.randomNumber:
            feedback = 'Too Low'
            self.attemptsMessage = f'Attempts: {self.attempts}'
            
        elif number == self.randomNumber:
            # Here the user has won, so we load the winning page.
            self.loadWinningPage()
            feedback = 'YOU WON!!!'
            self.attemptsMessage = (f'You made {self.attempts} attempts.')
            
        self.changingText.set(feedback)
        self.attemptsStatement.set(self.attemptsMessage)
            
game = App()
game.mainloop()