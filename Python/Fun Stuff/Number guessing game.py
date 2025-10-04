from logging import PlaceHolder
from tkinter import StringVar
import customtkinter as ctk
from random import choice

from numpy import delete

class App(ctk.CTk):
    def __init__(self):
        
        super().__init__()
        
        # Initialize the root window.
        self.title('Number Guessing Game')
        self.geometry('500x600+400+100')
        self.config(background="#D7C3C3")
        
        # Initialize the game attributes.
        self.changingText = StringVar(value='Pick A Number')
        self.randomNumber = choice(range(101))
        self.attempts = 0
        self.attemptsStatement = StringVar(value=f'Attempts: {self.attempts}')
        self.bgColour = '#D7C3C3'
        
        self.addChangingLabel(self.changingText, 60, "#202109", 40)
        self.addEntryBox()
        self.addChangingLabel(self.attemptsStatement, 30, "#0A4207", 5)
        self.addButton()
        
    def addLabel(self, text, colour='white'):
        self.label = ctk.CTkLabel(self, text=text, font=('Arial', 40), bg_color=self.bgColour, text_color=colour)
        self.label.pack(pady=20)
        
    def addEntryBox(self):
        self.entry = ctk.CTkEntry(self, width=300, height=60, font=('Arial', 40))
        self.entry.pack(pady=20)
        
    def addChangingLabel(self, textvariable, font_size, text_color, pad_value):
        self.label = ctk.CTkLabel(self, textvariable=textvariable, font=('Arial', font_size), bg_color=self.bgColour, text_color=text_color)
        self.label.pack(pady=pad_value)
        
    def addButton(self):
        self.button = ctk.CTkButton(self, text='GUESS', font=('Bauhaus 93', 30), command=self.guess)
        self.button.pack(pady=20)
        
    def guess(self):
        # Access the content of the entry box.
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
        number = int(number)
        if number > self.randomNumber:
            self.changingText.set(f'Too High')
            
        elif number < self.randomNumber:
            self.changingText.set(f'Too Low')
            
        elif number == self.randomNumber:
            self.changingText.set(f'You Won')
            
        # Increase the number of attempts by one.
        self.attempts += 1
        self.attemptsStatement.set(f'Attempts: {self.attempts}')
            
game = App()
game.mainloop()
