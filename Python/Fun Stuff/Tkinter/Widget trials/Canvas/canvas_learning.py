import tkinter as tk

# Initializing and configuring the root.
root = tk.Tk()
root.title('Tkinter Canvas Mastery')
root.geometry('600x400+350+100')

# Creating a canvas.
canvas = tk.Canvas(root, bg="#87BD87")
canvas.pack(fill=tk.BOTH, expand=True)

# Draw a rectangle.
# The first two attributes - x0 and y0 - move the shape to the right and down respectively.
# The 3rd and 4th attributes - x1 and y1 - increase the shape's width and height respectively.
canvas.create_rectangle(300, 50, 150, 100, fill="#87B5BD")

# Make other shapes.
canvas.create_oval(200, 200, 40, 70, fill="#6D6CB6", outline='yellow')
canvas.create_line(50, 50, 150, 100)

# Handling User Inputs.
# Respondding to mouse clicks.
def on_click(event):
    x, y = event.x, event.y
    canvas.create_oval(x+15, y+10, x-15, y-10, fill='yellow')
    

canvas.bind('<Button-1>', on_click)

root.mainloop()