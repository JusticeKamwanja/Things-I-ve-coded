import customtkinter as ctk

app = ctk.CTk()

# 1. Define your variable name and the "magic" color value
# Usually, people use a color they won't use elsewhere, like a specific lime green
MY_TRANSPARENT_COLOR = "#000001" # Nearly black, but unique

# 2. Tell the window to treat this specific color as invisible
# On Windows, this removes the color and allows clicks to pass through
app.config(background=MY_TRANSPARENT_COLOR)
app.attributes("-transparentcolor", MY_TRANSPARENT_COLOR)

# 3. Create a frame that ISN'T transparent so you have something to look at
main_ui = ctk.CTkFrame(app, fg_color="gray10", corner_radius=20)
main_ui.pack(expand=True, fill="both", padx=50, pady=50)

label = ctk.CTkLabel(main_ui, text="The area outside this frame is invisible!")
label.pack(pady=20)

app.mainloop()