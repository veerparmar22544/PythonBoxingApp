import tkinter as tk
from database import get_practice_logs

class Stats:
    def __init__(self, container, user_id):
        self.user_id = user_id  # User ID for identifying the user
        self.frame = tk.Frame(container)  # Create a frame for this page
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.columnconfigure(0, weight=1)  # Make the column expand to fill the available space

        # Title and Description
        tk.Label(self.frame, text="Statistics", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)  # Page title
        tk.Label(self.frame, text="View your practice session logs and stats.", font=("Helvetica", 12)).grid(row=1, column=0, columnspan=2, pady=5)  # Page description

        # Display Logs Button
        self.display_logs_button = tk.Button(self.frame, text="Display Logs", command=self.display_logs)  # Button to display logs
        self.display_logs_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Logs Display Area
        self.logs_display = tk.Text(self.frame, width=50, height=10, state=tk.DISABLED)  # Text widget to display logs
        self.logs_display.grid(row=3, column=0, columnspan=2, pady=10)

    def display_logs(self):
        # Enable the text widget to modify its content
        self.logs_display.config(state=tk.NORMAL)
        self.logs_display.delete("1.0", tk.END)  # Clear the current content
        logs = get_practice_logs(self.user_id)  # Retrieve the practice logs for the user
        for log in logs:
            # Insert each log entry into the text widget
            self.logs_display.insert(tk.END, f"{log[2]} (Timestamp: {log[3]})\n")
        # Disable the text widget to prevent further modification
        self.logs_display.config(state=tk.DISABLED)
