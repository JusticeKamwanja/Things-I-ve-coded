import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(' ' * 50 + 'Random Widgets')
        self.geometry('500x500+450+100')
        self.resizable(False, False)
        
        self.pad = 10
        self.menuVar = 'Hi'
        self.items = ['1', 'yrrrr', '65', 'Hi', 'Another choice']
        self.config(background="#A3E6A4")
        
        self.addWidgets()
        
    def addWidgets(self):    
        # Adding an options menu.
        menu = ctk.CTkOptionMenu(self, values=self.items, anchor='s')
        menu.grid(pady=self.pad, column=0, row=0)
        
        # Adding a progress bar.
        bar = ctk.CTkProgressBar(self, orientation='horizontal', progress_color="#e8f5ba", mode=['indeterminate', 'determinate'], determinate_speed=5, indeterminate_speed=5.0, height=20)
        bar.grid(pady=self.pad, padx=self.pad, column=1, row=0)
        
        # Adding a radio button.
        # button = ctk.CTk(self, fg_color=)
        # button.grid(pady=self.pad, padx=self.pad, column=2, row=0)
        pass

        # Adding a scrollable frame.
        self.frame = ctk.CTkScrollableFrame(self, width=100, height=10)
        self.frame.grid(pady=self.pad, padx=self.pad, column=3, row=0)
        
        # dding a label.
        for i in range(100):
            label = ctk.CTkLabel(self.frame, text='Example Text')
            label.pack()
        
        # Adding a scrollba.
        scrollBar = ctk.CTkScrollbar(self, command=self.move)
        scrollBar.grid(pady=self.pad, padx=self.pad, column=0, row=1)
        
        segmntedButton = ctk.CTkSegmentedButton(self)
        segmntedButton.grid(column=1, row=1)
        
        slider = ctk.CTkSlider(self)
        slider.grid(column=2, row=1)
        
    def move(self):
        self.config(background="#9EBBFB")
        
app = App()
app.mainloop()