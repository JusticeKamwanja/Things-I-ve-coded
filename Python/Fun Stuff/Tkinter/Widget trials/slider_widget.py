import customtkinter as ctk


class SliderWidget(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Slider Widget Example')
        self.geometry('420x320')

        # Label that shows current slider value
        self.value_label = ctk.CTkLabel(self, text='Value: 50', font=('Arial', 16))
        self.value_label.pack(pady=(20, 6))

        # A colour preview frame that will change as the slider moves
        self.color_preview = ctk.CTkFrame(self, width=200, height=80, corner_radius=8)
        self.color_preview.pack(pady=6)

        # Create a horizontal slider (0-100) with an update callback
        self.slider = ctk.CTkSlider(self, from_=0, to=100, number_of_steps=100, command=self.on_slider_change)
        self.slider.set(50)
        self.slider.pack(pady=12, padx=30, fill='x')

        # Reset button to return slider to default
        self.reset_btn = ctk.CTkButton(self, text='Reset', command=self.reset_slider)
        self.reset_btn.pack(pady=(6, 18))

        # Initialize preview colour
        self._update_preview(50)

    def on_slider_change(self, value):
        # CTkSlider passes float values; convert and update UI
        v = int(round(float(value)))
        self.value_label.configure(text=f'Value: {v}')
        self._update_preview(v)

    def _update_preview(self, value: int):
        """Update the colour preview. We'll map 0-100 to a blue->red gradient."""
        # map value to RGB between blue (0) and red (100)
        r = int(round((value / 100) * 255))
        g = 60
        b = int(round(((100 - value) / 100) * 255))
        hexcol = f'#{r:02x}{g:02x}{b:02x}'
        # CTkFrame uses `fg_color` for background
        self.color_preview.configure(fg_color=hexcol)

    def reset_slider(self):
        self.slider.set(50)
        self.on_slider_change(50)


app = SliderWidget()
if __name__ == '__main__':
    app.mainloop()