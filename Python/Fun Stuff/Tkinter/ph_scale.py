# Create a pH scale.

from tkinter import StringVar
import customtkinter as ctk


class PHScale(ctk.CTk):
    def __init__(self, fg_color="#008000"):
        super().__init__(fg_color=fg_color)
        self.title('Digital pH Scale')
        self.geometry('480x500+400+100')

        # State
        self.current_ph = 7
        self.ph_report = StringVar(value=f'Current pH: {self.current_ph}')

        # Colours for each pH value
        self.ph_colours = {
            1: "#FF0000",
            2: "#FF4500",
            3: "#FFA500",
            4: "#FFD700",
            5: "#FFFF00",
            6: "#9ACD32",
            7: "#008000",
            8: "#008080",
            9: "#0000FF",
            10: "#4B0082",
            11: "#8A2BE2",
            12: "#A020F0",
            13: "#8B008B",
            14: "#9400d3",
        }

        # Build UI
        self._create_widgets()
        self._apply_colour()

    def _create_widgets(self):
        self.title_label = ctk.CTkLabel(self, text='Explore the pH Scale', font=('Comic Sans MS', 30), text_color="#000000")
        self.title_label.grid(pady=10, row=0, column=0, columnspan=4)

        self.value_label = ctk.CTkLabel(self, textvariable=self.ph_report, font=('Comic Sans MS', 30), text_color="#000000")
        self.value_label.grid(pady=10, row=1, column=0, columnspan=4)

        self.decrease_button = ctk.CTkButton(self, width=140, height=28, text='Decrease pH', command=lambda: self.change_ph(-1))
        self.decrease_button.grid(row=2, column=1, padx=50)

        self.increase_button = ctk.CTkButton(self, width=140, height=28, text='Increase pH', command=lambda: self.change_ph(1))
        self.increase_button.grid(row=2, column=2, padx=50)

        self._update_buttons()

    def _apply_colour(self):
        colour = self.ph_colours.get(self.current_ph, "#FFFFFF")
        self.configure(fg_color=colour)
        self.title_label.configure(fg_color=colour)
        self.value_label.configure(fg_color=colour)

    def change_ph(self, delta: int):
        """Change the current pH by delta (-1 or +1)."""
        new = self.current_ph + delta
        if not (1 <= new <= 14):
            return

        self.current_ph = new
        self.ph_report.set(f'Current pH: {self.current_ph}')
        self._apply_colour()
        self._update_buttons()

    def _update_buttons(self):
        self.decrease_button.configure(state='normal' if self.current_ph > 1 else 'disabled')
        self.increase_button.configure(state='normal' if self.current_ph < 14 else 'disabled')


if __name__ == '__main__':
    app = PHScale()
    app.mainloop()