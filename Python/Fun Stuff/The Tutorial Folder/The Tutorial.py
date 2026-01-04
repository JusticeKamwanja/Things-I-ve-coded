# Import the library
import customtkinter as ctk

# Create the main application window
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.title("CustomTkinter Tutorial")
        self.geometry("550x500+400+100")

        # Create a label
        self.label = ctk.CTkLabel(self, text="Hello, CustomTkinter!", font=("Arial", 20))
        self.label.pack(pady=20)

        # Create a button
        self.button = ctk.CTkButton(self, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        self.label.configure(text="Button Clicked!")
        
app = App()
if __name__ == "__main__":
    app.mainloop()