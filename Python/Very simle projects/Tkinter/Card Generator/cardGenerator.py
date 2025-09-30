import customtkinter as ctk
from PIL import Image
import os
from os import listdir
from random import choice



class cardGenerator(ctk.CTk):
    # Initialize everything.
    def __init__(self):
        super().__init__()
        
        # Customize the root window.
        self.title('Random Card Generator')
        self.geometry('600x700+400+10')
        self.config(bg="#000000")
        ctk.set_appearance_mode('System')
        ctk.set_default_color_theme('green')
        
        
        # Pick a random image from the images folder.
        self.allImages = listdir('Images')

        # Initializing a counter to keep track of the button clicks.
        self.buttonClicks = 0

        # Keep a reference to the current CTkImage so it isn't garbage collected.
        self.my_pic = None
        
        self.addLabel()
        self.addButton()
                                                                                                                                               
    def removeCurrentImage(self):
        # Destroy any existing card label (but not the button)
        for widget in list(self.winfo_children()):
            if widget is not self.button and widget is not self.welcomeLabel:
                widget.destroy()
        
    def addLabel(self):
        self.welcomeLabel = ctk.CTkLabel(self, width=350, fg_color='#000000', text_color="black", font=('Bahaus 93', (40)), text='Generate your card!!')
        self.welcomeLabel.pack(pady=40)
        
    def addButton(self):
        self.button = ctk.CTkButton(self, text='Generate', command=self.addImage, font=('comic sans ms', (20)))
        self.button.pack(padx=20)
        
    def addImage(self):
        '''If it is the first click, add a random image.
        If it is any subsequent click, remove the current image and add another random image'''
        # Each click should pick a new random image and create a new CTkImage.
        # Pick a random image file name and build a safe path.
        chosenImage = choice(self.allImages)
        self.image_path = f"Images{os.sep}{chosenImage}"

        # Initiate a title for every card displayed.    
        self.cardName = self.image_path.removeprefix("Images\.").removesuffix('.jpg')
        
        # Open the PIL image and convert into a CTkImage for display.
        pil_image = Image.open(self.image_path)

        # Create a CTkImage to display the card.
        self.my_pic = ctk.CTkImage(dark_image=pil_image, size=(280, 340))

        # Remove previous card (if any) then add new label.
        self.removeCurrentImage()
        self.cardImage = ctk.CTkLabel(self, text=self.cardName, font=('Bahaus 93', (30)), image=self.my_pic, compound='bottom', bg_color='#000000')
        self.cardImage.pack(pady=20)
        
        # Track clicks (kept for compatibility with original logic).
        self.buttonClicks += 1


app = cardGenerator()

app.mainloop()