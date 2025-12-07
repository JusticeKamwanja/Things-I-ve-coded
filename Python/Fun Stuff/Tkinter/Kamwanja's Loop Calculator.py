'''I am going to try and make a calculator. The buttons are going to be created using a loop, hence the name, Loop Calculator'''

from tkinter import StringVar
import customtkinter as ctk
from functools import partial


class Calculator(ctk.CTk):
    def __init__(self, fg_color="#F39FC6"):
        super().__init__(fg_color)
        
        '''Initalize the root window'''
        self.title("Kamwanja's Loop Calculator")
        self.geometry('+100+60')
        # self.resizable(False, False)
        
        # Initiate other attributes.
        self.equation = StringVar(value='The equation goes here')
        self.answer = StringVar(value='Answer')
        self.symbols = ['÷', '+',  '-',  'x', '%', '()', '<', '=', '٠', ' ±']
        
        # Add the top frame to house the butttons.
        self.equationLabel()
        self.addAnswer()
        self.addFrame()
        
        self.addButtons()
        
    def addFrame(self):
        self.frame = ctk.CTkFrame(self, width=350, height=100, corner_radius=5, fg_color="#414A40")
        self.frame.grid(row=2, column=0, columnspan=4, padx=1, pady=1)
        
    def equationLabel(self):
        self.answerLabel = ctk.CTkLabel(self, 60, 50, textvariable=self.equation, text_color="#123390", font=('Comic Sans MS', 25), bg_color='grey')
        self.answerLabel.grid(row=0, column=1, sticky='ew')
        
    def addAnswer(self):
        self.answerLabel = ctk.CTkLabel(self, 60, 50, textvariable=self.answer, text_color="#123390", font=('Comic Sans MS', 25), bg_color='grey')
        self.answerLabel.grid(row=1, column=1, sticky='e')
        
    def checkCurrentEquationState(self, symbol):
        '''Checking the equation to prevent entering two symbols'''
        if self.currentText:
            self.currentText = self.equation.get() 
            index = len(self.currentText) -1
            lastClick = self.currentText[index]
            
            # If the last click was not a symbol, the click will return an output.
            if lastClick not in self.symbols:
                equationOutput = self.currentText + symbol
            
            # If the user clicks the same symbol twice, the subsequent clicks will be ignored.
            if lastClick in self.symbols and lastClick == symbol:
                equationOutput = self.currentText
                
            # If the user clicks the minus sign right after the plus sign, before clicking another number, the minus will replace the plus.
            if lastClick in self.symbols and lastClick != symbol:
                equationOutput = self.currentText[:index] + symbol
                
        else:
            # If there is no text.
                equationOutput = self.currentText
            
        return equationOutput
        
    def addEquation(self, text):
        '''Manipulate the label according to the button pushed.'''
        # There are a few types of texts to be processed.
        # The symbols, the numbers and the 'del' key.
        
        # Access the current label text.
        self.currentText = self.equation.get()
        self.output =''
        
        if str(text) == 'del':
            # When the user hits the 'del' key, delete everything.
            self.output = ''

        if str(text) in self.symbols:
            # If the text is a symbol, it may need more processing.
            if text == '()':
                pass
            if text == '<':
                self.output = self.currentText[:-1]
                
            # if text == '٠': 
            #     pass
            # if text == '±':
            #     pass
            if text == '=':
                answer = self.process(self.currentText)
                self.answer.set(answer)
                self.output = self.currentText
            else:
                # If the text is not a symbol
                self.output = self.checkCurrentEquationState(text)

        # When the user clicks a number.
        numbers = [str(i) for i in range(0, 10)]
        
        if text in numbers:
            self.newText = self.currentText + text
            self.output = self.newText
    
        
        self.equation.set(self.output)
        
    def process(self, equation):
                
        """Changes the 'x' to '*', '÷ ' to '/'KO and evaluates the equation."""
        output = ''
        for i in equation:
            if i.lower() == 'x':
                output += '*'
            elif i == '÷':
                output += '/'
            else:
                output += i
                
        return eval(output)
                
    def addButtons(self):
        '''This will add the delete button first, then add the other 20 buttons using a loop'''
        
        # Add the first button.
        self.addButton(self.frame, text='del', hover_color="#ac1818", column=3, row=2, command=partial(self.addEquation, 'del'),text_color="#FFFFFF")
        
        # Initiating the button colours.
        # 'x' is the mainColour
        x = "#176888" # This colours the number buttons.
        y = "#583B05" # This colours the other buttons.
        z = "#6637E7" # This colours the symbol buttons.
        rowColour = [z] + [x] * 3 # This gves one green, and three white buttons.
        rowOne = [z] + [z]*2 + [y] 
        firstRowsColours = rowOne + rowColour * 3 # This will colour the first four rows.
        lastRowColours = ["#079E11"] + [z] + [x] + [z] # This will give the last row one blue, and three black buttons.
        # Concatenate the row colour lists to initiate the entire button colour scheme.
        buttonColours = firstRowsColours + lastRowColours
        
        # Initiating the butontext colours.
        # 'x' is the mainColour
        x = "#FFFFFF"
        rowColour = ["#F1ACAC"] + [x] * 3
        
        firsttextsColours = rowColour * 4 # This will repeat the colour onto the first four rows.
        lasttextColours = ["#FFFFFF"] + [x] * 3 # This will give the last row one blue, and three black buttons.
        # Concatenate the row colour lists to initiate the entire button colour scheme.
        textColours = firsttextsColours + lasttextColours
        
        
        buttonTexts = ['÷', '%', '()', '<', 'X', '7', '8', '9', '-', '4', '5', '6', '+', '1', '2', '3', '=', '٠', '0', '±']
        rows = list(range(3, 7 + 1))
        buttonRows = []
        columns = [0, 1, 2, 3] * 5
        for x in rows:
            for i in range(4):
                buttonRows.append(x)
                
        # This adds the rest of the buttons.
        for buttonColour, buttonText, buttonRow, column, textColour in zip(buttonColours, buttonTexts, buttonRows, columns, textColours):
            # This for loop will loop through the lists mentioned.
            self.addButton(self.frame,
                           text=buttonText,
                           hover_color=buttonColour,
                           column=column,
                           row=buttonRow,
                           command=partial(self.addEquation, buttonText),
                           text_color=textColour)
               
    def addButton(self, master, text, hover_color, column, row, command, fg_color="#221F1F", image=None, text_color=None):
        self.button = ctk.CTkButton(master=master, text=text, hover_color=hover_color, corner_radius=0, font=('Anurati', 25), width=80, height=50, command=command, fg_color=fg_color, image=image, text_color=text_color)
        # Pack the button
        self.button.grid(row=row, column=column, pady=0, padx=0)
     
app = Calculator()
app.mainloop()



# Process the input when the user clicks a symbol.