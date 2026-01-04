# Create a pH scale.

from tkinter import StringVar
import customtkinter as ctk


class PHScale(ctk.CTk):
    def __init__(self, fg_color="#008000"):
        super().__init__(fg_color=fg_color)
        # remember the initial background colour so we can blend with black
        self.base_bg = fg_color
        self.title('Digital pH Scale')
        self.geometry('700x500+340+100')

        # Configure root grid so the center cell stays centered when window resizes
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)

        # State
        self.current_ph = 7
        self.ph_report = StringVar(value=f'Current pH: {self.current_ph}')
        self.transparent_color = "#CFCFFF"

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
        self.create_widgets()
        self.apply_colour()

    def create_widgets(self):
        # Create a centered content frame in the middle cell of the root grid
        heading_bg = self.blend_with_black(self.base_bg, 0.2)

        # Use the blended heading background for the content frame so both
        # frames share the same fg_color appearance.
        self.content_frame = ctk.CTkFrame(self, fg_color=heading_bg, border_width=0)
        self.content_frame.grid(row=1, column=1)

        # Use a solid colour that approximates 20% opaque black over the
        # current background by blending with black (some platforms ignore
        # alpha in widget colours). We'll use the same blended colour here.
        self.heading_frame = ctk.CTkFrame(self.content_frame, fg_color=heading_bg, border_width=0)
        self.heading_frame.grid(pady=20, padx=20, row=0, column=0, columnspan=2)

        self.title_label = ctk.CTkLabel(self.heading_frame, text='Explore the pH Scale', font=('Comic Sans MS', 30), text_color="#000000")
        self.title_label.grid(pady=10, row=0, column=0, columnspan=2)

        self.value_label = ctk.CTkLabel(self.heading_frame, textvariable=self.ph_report, font=('Comic Sans MS', 30), text_color="#000000")
        self.value_label.grid(pady=10, row=1, column=0, columnspan=2)

        # Create buttons inside the centered content frame
        self.decrease_button = ctk.CTkButton(self.content_frame, width=140, height=28, text='Decrease pH', text_color_disabled="#EEFF00", command=lambda: self.change_ph(-1))
        self.decrease_button.grid(row=1, column=0, padx=20, pady=25)

        self.increase_button = ctk.CTkButton(self.content_frame, width=140, height=28, text='Increase pH', text_color_disabled="#EEFF00", command=lambda: self.change_ph(1))
        self.increase_button.grid(row=1, column=1, padx=20, pady=25)
        self.update_buttons()

    def apply_colour(self):
        colour = self.ph_colours.get(self.current_ph, "#FFFFFF")
        self.configure(fg_color=colour)
        self.title_label.configure(fg_color=colour)
        self.value_label.configure(fg_color=colour)
        # Update heading frame to be the base colour blended with 20% black
        heading_bg = self.blend_with_black(colour, 0.2)
        # Keep content_frame and heading_frame in sync
        self.heading_frame.configure(fg_color=heading_bg)
        self.content_frame.configure(fg_color=heading_bg)

    def change_ph(self, deviation: int):
        """Change the current pH by deviation (-1 or +1)."""
        new_ph = self.current_ph + deviation
        # If the new pH is not in the valid range, ignore the button press.
        if not (1 <= new_ph <= 14):
            return

        self.current_ph = new_ph
        self.ph_report.set(f'Current pH: {self.current_ph}')
        self.apply_colour()
        self.update_buttons()

    def update_buttons(self):
        decrease_button_state = 'normal' if self.current_ph > 1 else 'disabled'
        increase_button_state = 'normal' if self.current_ph < 14 else 'disabled'
        # Update state and visual feedback (colour) based on the computed state
        self.decrease_button.configure(state=decrease_button_state, fg_color=("#221F1F" if decrease_button_state == 'disabled' else "#6F6FF0"))
        self.increase_button.configure(state=increase_button_state, fg_color=('#221F1F' if increase_button_state == 'disabled' else '#6F6FF0'))

    def blend_with_black(self, hex_color: str, alpha: float) -> str:
        """Return a solid hex colour that approximates overlaying black at
        `alpha` opacity on top of `hex_color`.
        """
        c = hex_color.lstrip('#')
        # If colour includes an alpha channel, drop it
        if len(c) == 8:
            c = c[:6]
        if len(c) != 6:
            return hex_color
        r = int(c[0:2], 16)
        g = int(c[2:4], 16)
        b = int(c[4:6], 16)
        r = int(round(r * (1 - alpha)))
        g = int(round(g * (1 - alpha)))
        b = int(round(b * (1 - alpha)))
        return f'#{r:02x}{g:02x}{b:02x}'

if __name__ == '__main__':
    app = PHScale()
    app.mainloop()