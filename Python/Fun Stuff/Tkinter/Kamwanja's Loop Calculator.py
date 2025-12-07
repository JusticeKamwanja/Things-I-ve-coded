'''I am going to try and make a calculator. The buttons are going to be created using a loop, hence the'''

from tkinter import StringVar
import customtkinter as ctk

class Calculator(ctk.CTk):
    def __init__(self, fg_color="#ECEE99"):
        super().__init__(fg_color)
        
        '''Initalize the root window'''
        self.title("Kamwanja's Loop Calculator")
        self.geometry('360x500+100+60')
        
        # Initiate other attributes.
        self.answer = StringVar(value='The answer goes here')
        
        # Add the top frame to house the butttons.
        self.addAnswer()
        self.addFrame()
        
        self.addButtons()
        
    def addFrame(self):
        self.frame = ctk.CTkFrame(self, width=350, height=100, corner_radius=5, fg_color="#4ABE32")
        self.frame.grid(row=2, column=0, columnspan=4, padx=5, pady=5)
        
    def addAnswer(self):
        self.answerLabel = ctk.CTkLabel(self, 60, 50, textvariable=self.answer, text_color="#123390", font=('Comic Sans MS', 25))
        self.answerLabel.grid(row=0, column=1, sticky='e')
        
        
    def addButtons(self):
        '''This will add the delete button first, then add the other 20 buttons using a loop'''
        
        # Add the first button.
        
        # Initiating the button colours.
        # 'x' is the mainColour
        x = "#3B3838"
        rowColour = ["#457947"] + [x] * 3 # This gves one green, and three white buttons.
        
        firstRowsColours = rowColour * 4 # This will repeat the colour onto the first four rows.
        lastRowColours = ["#6CC1F1"] + [x] * 3 # This will give the last row one blue, and three black buttons.
        # Concatenate the row colour lists to initiate the entire button colour scheme.
        buttonColours = firstRowsColours + lastRowColours
        
        buttonTexts = ['/', '%', '()', 'c', 'X', '7', '8', '9', '--', '4', '5', '6', '+', '1', '2', '3', '=', '.', '0', 'n']
        rows = list(range(3, 7 + 1))
        buttonRows = []
        columns = [0, 1, 2, 3] * 5
        for x in rows:
            for i in range(4):
                buttonRows.append(x)
                
        # This adds the buttons.
        for buttonColour, text, buttonRow, column in zip(buttonColours, buttonTexts, buttonRows, columns):
            self.addButton(self.frame, text=text, width=70, height=70,  fg_color=buttonColour, column=column, row=buttonRow)
               
    def addButton(self, master, text, width, height, fg_color, column, row):
        self.button = ctk.CTkButton(master=master, text=text, width=width, height=height, fg_color=fg_color, corner_radius=1000, font=('aNURATI', 20))
        self.button.grid(row=row, column=column)
     

        
app = Calculator()
app.mainloop()



# Create a function to handle all buttons instead of a lambda. the function takes an argument that it gets from the button implemntation