import tkinter as tk
from database import update_calorie_count, get_calorie_count  # Add these functions in database.py

class CalorieCounter:
    def __init__(self, container, user_id):
        self.user_id = user_id
        self.total_calories = get_calorie_count(self.user_id)  # Fetch initial calorie count from database

        self.frame = tk.Frame(container)
        self.frame.grid(row=0, column=0, sticky="nsew")

        # Title
        tk.Label(self.frame, text="Calorie Counter", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=3, pady=10)

        # Total Calorie Display
        self.calorie_label = tk.Label(self.frame, text=f"Total Calories: {self.total_calories}", font=("Helvetica", 14))
        self.calorie_label.grid(row=1, column=0, columnspan=3, pady=10)

        # Input Box
        self.calorie_input = tk.Entry(self.frame, width=10)
        self.calorie_input.grid(row=2, column=0, columnspan=3, pady=5)

        # Add/Minus Buttons
        self.add_button = tk.Button(self.frame, text="Add 100 Calories", command=self.add_calories)
        self.add_button.grid(row=3, column=0, pady=5)

        self.minus_button = tk.Button(self.frame, text="Minus 100 Calories", command=self.minus_calories)
        self.minus_button.grid(row=3, column=2, pady=5)

        # Input Button
        self.input_button = tk.Button(self.frame, text="Add Input Calories", command=self.add_input_calories)
        self.input_button.grid(row=4, column=0, columnspan=3, pady=5)

    def update_calorie_label(self):
        self.calorie_label.config(text=f"Total Calories: {self.total_calories}")

    def add_calories(self):
        self.total_calories += 100
        update_calorie_count(self.user_id, self.total_calories)
        self.update_calorie_label()

    def minus_calories(self):
        self.total_calories -= 100
        update_calorie_count(self.user_id, self.total_calories)
        self.update_calorie_label()

    def add_input_calories(self):
        try:
            input_calories = int(self.calorie_input.get())
            self.total_calories += input_calories
            update_calorie_count(self.user_id, self.total_calories)
            self.update_calorie_label()
            self.calorie_input.delete(0, tk.END)
        except ValueError:
            # Handle invalid input
            pass
