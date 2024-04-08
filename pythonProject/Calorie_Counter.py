import tkinter as tk

class CalorieCounter:
    def __init__(self, container):
        self.frame = tk.Frame(container)
        tk.Label(self.frame, text="This is Calorie Counter Page", ).pack()
        tk.Text(self.frame, height=10, width=50).pack()  # Add a text box
