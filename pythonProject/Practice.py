import tkinter as tk

class Practice:
    def __init__(self, container):
        self.frame = tk.Frame(container)
        tk.Label(self.frame, text="This is Practice page").pack()

        canvas = tk.Canvas(self.frame, width=400, height=400)
        canvas.pack()

        # Coordinates for the center of the canvas
        center_x = 200
        center_y = 200

        # Draw a circle with radius 100 centered at (center_x, center_y)
        canvas.create_oval(center_x - 100, center_y - 100, center_x + 100, center_y + 100, fill="white")

