import tkinter as tk
import time
from database import add_practice_log  # Add this function in database.py

class Practice:
    def __init__(self, container, user_id):
        self.user_id = user_id
        self.frame = tk.Frame(container)
        self.frame.grid(row=0, column=0, sticky="nsew")

        # Title and Description
        tk.Label(self.frame, text="Practice Session", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self.frame, text="Log your practice sessions and visualize your techniques.",
                 font=("Helvetica", 12)).grid(row=1, column=0, columnspan=2, pady=5)

        # Timer
        self.time_label = tk.Label(self.frame, text="00:00:00", font=("Helvetica", 40))
        self.time_label.grid(row=2, column=0, columnspan=2, pady=5)
        self.start_time = None
        self.running = False

        # Start/Stop button
        self.timer_button = tk.Button(self.frame, text="Start Timer", command=self.toggle_timer)
        self.timer_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Log Textbox
        self.log_label = tk.Label(self.frame, text="Practice Log:", font=("Helvetica", 12))
        self.log_label.grid(row=4, column=0, columnspan=2, pady=5)
        self.log_text = tk.Text(self.frame, width=50, height=10)
        self.log_text.grid(row=5, column=0, columnspan=2, pady=10)

        # Save Log Button
        self.save_log_button = tk.Button(self.frame, text="Save Log", command=self.save_log)
        self.save_log_button.grid(row=6, column=0, columnspan=2, pady=10)

    def toggle_timer(self):
        if self.running:
            self.running = False
            self.timer_button.config(text="Start Timer")
        else:
            if not self.start_time:
                self.start_time = time.time()
            self.running = True
            self.timer_button.config(text="Stop Timer")
            self.update_timer()

    def update_timer(self):
        if self.running:
            elapsed_time = int(time.time() - self.start_time)
            hours, minutes, seconds = elapsed_time // 3600, (elapsed_time % 3600) // 60, elapsed_time % 60
            self.time_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
            self.frame.after(1000, self.update_timer)

    def save_log(self):
        log_text = self.log_text.get("1.0", tk.END).strip()
        if log_text:
            add_practice_log(self.user_id, log_text)
            self.log_text.delete("1.0", tk.END)
