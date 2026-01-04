# Import the library
import customtkinter as ctk
from matplotlib.pylab import choice

# Create the main application window
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.title("CustomTkinter Tutorial")
        self.geometry("550x500+400+100")
        
        # Create a button
        self.button = ctk.CTkButton(self, text="Example Button", bg_color="red", hover_color="green", border_color="black", border_width=1, border_spacing=20)
        self.button.pack(pady=100)
        
        # Create a combo box
        self.combobox_var = ctk.StringVar(value="option 2")
        self.combobox = ctk.CTkComboBox(self, values=["option 1", "option 2"], command=combobox_callback, variable=self.combobox_var)
        self.combobox.pack(pady=20)
        
def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

app = App()
if __name__ == "__main__":
    app.mainloop()