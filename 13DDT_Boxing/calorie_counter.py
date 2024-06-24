import tkinter as tk
from database import update_calorie_count, get_calorie_count


class CalorieCounter:
    def __init__(self, container, user_id):
        self.user_id = user_id
        self.frame = tk.Frame(container)

        tk.Label(self.frame, text="Calorie Counter Page").pack()

        self.calorie_count = get_calorie_count(self.user_id)
        self.calorie_label = tk.Label(self.frame, text=f"Total Calories: {self.calorie_count}", font=("Helvetica", 16))
        self.calorie_label.pack()

        tk.Button(self.frame, text="Add 100 Calories", command=self.add_calories).pack()
        tk.Button(self.frame, text="Subtract 100 Calories", command=self.subtract_calories).pack()

        tk.Label(self.frame, text="Input Calories:").pack()
        self.calorie_input = tk.Entry(self.frame)
        self.calorie_input.pack()
        tk.Button(self.frame, text="Set Calories", command=self.set_calories).pack()

        tk.Button(self.frame, text="Reset to Zero", command=self.reset_calories).pack()

    def add_calories(self):
        self.calorie_count += 100
        self.update_calorie_display()

    def subtract_calories(self):
        self.calorie_count -= 100
        self.update_calorie_display()

    def set_calories(self):
        try:
            calories = int(self.calorie_input.get())
            self.calorie_count = calories
            self.update_calorie_display()
        except ValueError:
            pass  # Handle invalid input if necessary

    def reset_calories(self):
        self.calorie_count = 0
        self.update_calorie_display()

    def update_calorie_display(self):
        self.calorie_label.config(text=f"Total Calories: {self.calorie_count}")
        update_calorie_count(self.user_id, self.calorie_count)
