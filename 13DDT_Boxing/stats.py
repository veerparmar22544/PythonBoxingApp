import tkinter as tk

class Stats:
    def __init__(self, container):
        self.frame = tk.Frame(container)
        tk.Label(self.frame, text="This is stats Page").pack()
        tk.Text(self.frame, height=10, width=50).pack()  # Add a text box

