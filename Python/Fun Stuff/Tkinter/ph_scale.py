# Create a pH scale.

from tkinter import StringVar
import customtkinter as ctk
from functools import partial

class PHScale(ctk.CTk):
    def __init__(self, fg_color="#008000"):
        super().__init__(fg_color)
        # Initialize the root window and other attributes.
        self.title('Digital pH Scale')
        self.geometry('480x500+400+100')
        
        self.currentPH = 7
        self.pHReport =StringVar(value='Current pH: 7')
        self.currentBackground = None
        
        self.pHColours = {
            1:"#FF0000",
            2:"#FF4500",
            3:"#FFA500",
            4:"#FFD700",
            5:"#FFFF00",
            6:"#9ACD32",
            7:"#008000",
            8:"#008080",
            9:"#0000FF",
            10:"#4B0082",
            11:"#8A2BE2",
            12:"#A020F0",
            13:"#8B008B",
            14:"#9400d3",}
        
        
        self.runApp()
        
    def runApp(self):
        '''A function to run the whole application.'''
        buttonTexts = ['Decrease pH', 'Increase pH']
        buttonRows = [2, 2]
        buttoncolumns = [1, 2]
        # Add the two buttons.
        for text, row, column in zip(buttonTexts, buttonRows, buttoncolumns):
            self.addButton(text, partial(self.changePH, text), row, column)
        # Add the label spanning four colimns.
        self.addLabel('Explore the pH Scale', 0, 0, 4)
        self.addChangingLabel(self.pHReport, 1, 0, 4)
            
    def addButton(self, text, command, row, column):
        button = ctk.CTkButton(self, 140, 28, text=text, command=command)
        button.grid(row=row, column=column, padx=50)
        
    def addLabel(self, text, row, column, columnspan):
        label = ctk.CTkLabel(self, text=text, font=('comic sans MS', 30), text_color="#000000", fg_color=self.pHColours[self.currentPH])
        label.grid(pady=10, row=row, column=column, columnspan=columnspan)

    def addChangingLabel(self, text, row, column, columnspan):
        label = ctk.CTkLabel(self, textvariable=text, font=('comic sans MS', 30), text_color="#000000", fg_color=self.pHColours[self.currentPH])
        label.grid(pady=10, row=row, column=column, columnspan=columnspan)

    def changePH(self, button_text):
        # Ignore the input if the current pH is above 14 or below 1.
        error_message = 'pH values range from 1 to 14'
        if button_text.lower() == 'increase ph':
            if self.currentPH == 14:
                output = error_message

            else:
                self.currentPH += 1
                output = f'Current pH: {self.currentPH}'
            
        if button_text.lower() == 'decrease ph':
            if self.currentPH == 1:
                output = error_message
            else:
                self.currentPH -= 1
                output = f'Current pH: {self.currentPH}'
            
        # Change the background colour and the pH report.
        
        self.pHReport.set(output)
        self.newBackgroundColour  = self.pHColours[self.currentPH]
        self.config(background=self.newBackgroundColour)
        
app = PHScale()
if __name__ == '__main__':
    app.mainloop()