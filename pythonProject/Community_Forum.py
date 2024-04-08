import tkinter as tk

class CommunityForum:
    def __init__(self, container):
        self.frame = tk.Frame(container)
        tk.Label(self.frame, text="This is Community Forum Page").pack()
        tk.Text(self.frame, height=10, width=50).pack()  # Add a text box
