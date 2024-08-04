import tkinter as tk
from database import update_calorie_count, get_calorie_count

class CalorieCounter:
    def __init__(self, container, user_id):
        self.user_id = user_id  # User ID for identifying the user
        self.frame = tk.Frame(container)  # Create a frame for this page
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.columnconfigure(0, weight=1)  # Make the column expand to fill the available space

        # Create and place a label for the page title
        tk.Label(self.frame, text="Calorie Counter Page").grid(row=0, column=0, pady=10)

        # Retrieve the current calorie count for the user
        self.calorie_count = get_calorie_count(self.user_id)
        # Create and place a label to display the calorie count
        self.calorie_label = tk.Label(self.frame, text=f"Total Calories: {self.calorie_count}", font=("Helvetica", 16))
        self.calorie_label.grid(row=1, column=0, pady=10)

        # Create and place a button to add 100 calories
        tk.Button(self.frame, text="Add 100 Calories", command=self.add_calories).grid(row=2, column=0, pady=5)
        # Create and place a button to subtract 100 calories
        tk.Button(self.frame, text="Subtract 100 Calories", command=self.subtract_calories).grid(row=3, column=0, pady=5)

        # Create and place a label and entry for manual calorie input
        tk.Label(self.frame, text="Input Calories:").grid(row=4, column=0, pady=10)
        self.calorie_input = tk.Entry(self.frame)
        self.calorie_input.grid(row=5, column=0, pady=5)
        tk.Button(self.frame, text="Set Calories", command=self.set_calories).grid(row=6, column=0, pady=5)

        # Create and place a button to reset the calorie count to zero
        tk.Button(self.frame, text="Reset to Zero", command=self.reset_calories).grid(row=7, column=0, pady=5)

    def add_calories(self):
        # Add 100 calories to the current count
        self.calorie_count += 100
        self.update_calorie_display()

    def subtract_calories(self):
        # Subtract 100 calories from the current count
        self.calorie_count -= 100
        self.update_calorie_display()

    def set_calories(self):
        # Set the calorie count to the value entered by the user
        try:
            calories = int(self.calorie_input.get())
            self.calorie_count = calories
            self.update_calorie_display()
        except ValueError:
            pass  # Handle invalid input if necessary

    def reset_calories(self):
        # Reset the calorie count to zero
        self.calorie_count = 0
        self.update_calorie_display()

    def update_calorie_display(self):
        # Update the label to display the current calorie count
        self.calorie_label.config(text=f"Total Calories: {self.calorie_count}")
        # Update the calorie count in the database
        update_calorie_count(self.user_id, self.calorie_count)
