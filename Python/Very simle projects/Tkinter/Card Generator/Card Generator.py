import customtkinter as ctk
from PIL import Image, ImageTk
import os
from os import listdir
from random import choice



class cardGenerator(ctk.CTk):
    # Initialize everything.
    def __init__(self):
        super().__init__()
        
        # Customize the root window.
        self.title('Random Card Generator')
        self.geometry('400x500+500+120')
        ctk.set_appearance_mode('System')
        ctk.set_default_color_theme('dark-blue')
        
        # Pick a random image from the images folder.
        self.allImages = listdir('Images')

        # Initializing a counter to keep track of the button clicks.
        self.buttonClicks = 0

        # Keep a reference to the current CTkImage so it isn't garbage collected.
        self.my_pic = None
        
        self.addButton()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    def replaceCard(self):
        # Destroy any existing card label (but not the button)
        for widget in list(self.winfo_children()):
            if widget is not self.button:
                widget.destroy()
        
    def addButton(self):
        self.button = ctk.CTkButton(self, text='Show Image', command=self.addImage)
        self.button.pack(padx=20)
        
    def addImage(self):
        '''If it is the first click, add a random image.
        If it is any subsequent click, remove the current image and add another random image'''
        # Each click should pick a new random image and create a new CTkImage.
        # Pick a random image file name and build a safe path.
        chosen = choice(self.allImages)
        image_path = f"Images{os.sep}{chosen}"

        # Open the PIL image and convert into a CTkImage for display.
        pil_image = Image.open(image_path)

        # Create a CTkImage and store reference on self to avoid GC.
        self.my_pic = ctk.CTkImage(dark_image=pil_image, size=(200, 200))

        # Remove previous card (if any) then add new label.
        self.replaceCard()
        self.cardImage = ctk.CTkLabel(self, text='text goes here', image=self.my_pic, compound='top')
        self.cardImage.pack()
        
        # Track clicks (kept for compatibility with original logic).
        self.buttonClicks += 1


app = cardGenerator()

app.mainloop()