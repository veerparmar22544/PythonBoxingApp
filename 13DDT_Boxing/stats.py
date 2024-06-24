import tkinter as tk
from database import get_practice_logs

class Stats:
    def __init__(self, container, user_id):
        self.user_id = user_id
        self.frame = tk.Frame(container)
        self.frame.grid(row=0, column=0, sticky="nsew")

        # Title and Description
        tk.Label(self.frame, text="Statistics", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self.frame, text="View your practice session logs and stats.", font=("Helvetica", 12)).grid(row=1, column=0, columnspan=2, pady=5)

        # Display Logs Button
        self.display_logs_button = tk.Button(self.frame, text="Display Logs", command=self.display_logs)
        self.display_logs_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Logs Display Area
        self.logs_display = tk.Text(self.frame, width=50, height=10, state=tk.DISABLED)
        self.logs_display.grid(row=3, column=0, columnspan=2, pady=10)

    def display_logs(self):
        self.logs_display.config(state=tk.NORMAL)
        self.logs_display.delete("1.0", tk.END)
        logs = get_practice_logs(self.user_id)
        for log in logs:
            self.logs_display.insert(tk.END, f"{log[2]} (Timestamp: {log[3]})\n")
        self.logs_display.config(state=tk.DISABLED)

# Testing purposes
if __name__ == "__main__":
    root = tk.Tk()
    app = Stats(root, user_id=1)
    root.mainloop()
