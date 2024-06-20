import tkinter as tk

class Stats:
    def __init__(self, container, user_id):
        self.user_id = user_id
        self.frame = tk.Frame(container)
        self.frame.grid(row=0, column=0, sticky="nsew")

        # Title
        tk.Label(self.frame, text="Stats Page", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Text(self.frame, height=10, width=50).grid(row=1, column=0, columnspan=2, pady=10)  # Add a text box
