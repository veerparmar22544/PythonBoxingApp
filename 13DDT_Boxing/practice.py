import tkinter as tk
import time
from database import add_practice_log

class Practice:
    def __init__(self, container, user_id):
        self.user_id = user_id  # User ID for identifying the user
        self.frame = tk.Frame(container)  # Create a frame for this page
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.columnconfigure(0, weight=1)  # Make the column expand to fill the available space

        # Title and Description
        tk.Label(self.frame, text="Practice Session", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)  # Page title
        tk.Label(self.frame, text="Log your practice sessions and visualize your techniques.", font=("Helvetica", 12)).grid(row=1, column=0, columnspan=2, pady=5)  # Page description

        # Timer
        self.time_label = tk.Label(self.frame, text="00:00:00", font=("Helvetica", 40))  # Timer label
        self.time_label.grid(row=2, column=0, columnspan=2, pady=5)
        self.start_time = None  # Initialize start time
        self.running = False  # Timer state

        # Start/Stop button
        self.timer_button = tk.Button(self.frame, text="Start Timer", command=self.toggle_timer)  # Button to start/stop the timer
        self.timer_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Log Textbox
        self.log_label = tk.Label(self.frame, text="Practice Log:", font=("Helvetica", 12))  # Label for the practice log textbox
        self.log_label.grid(row=4, column=0, columnspan=2, pady=5)
        self.log_text = tk.Text(self.frame, width=50, height=10)  # Textbox for entering practice logs
        self.log_text.grid(row=5, column=0, columnspan=2, pady=10)

        # Save Log Button
        self.log_button = tk.Button(self.frame, text="Save Log", command=self.save_log)  # Button to save the practice log
        self.log_button.grid(row=6, column=0, columnspan=2, pady=10)

    def toggle_timer(self):
        if self.running:
            # Stop the timer
            self.running = False
            self.timer_button.config(text="Start Timer")
        else:
            # Start the timer
            if not self.start_time:
                self.start_time = time.time()
            self.running = True
            self.timer_button.config(text="Stop Timer")
            self.update_timer()

    def update_timer(self):
        if self.running:
            # Update the timer display every second
            elapsed_time = int(time.time() - self.start_time)
            hours, minutes, seconds = elapsed_time // 3600, (elapsed_time % 3600) // 60, elapsed_time % 60
            self.time_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
            self.frame.after(1000, self.update_timer)  # Call update_timer again after 1 second

    def save_log(self):
        log_text = self.log_text.get("1.0", tk.END).strip()  # Get the text from the log textbox
        if log_text:
            # Save the log if there is any text
            add_practice_log(self.user_id, log_text)
            self.log_text.delete("1.0", tk.END)  # Clear the log textbox
            print("Log saved")
