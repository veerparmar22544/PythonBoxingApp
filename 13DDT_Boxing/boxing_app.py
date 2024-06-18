import tkinter as tk
from calorie_counter import CalorieCounter
from practice import Practice
from stats import Stats

class Boxing_App(tk.Tk):
    def __init__(self, user_id, app_name="Boxing App"):
        super().__init__()
        self.user_id = user_id
        self.app_name = app_name
        self.setup()

    def setup(self):
        self.title(self.app_name)
        self.geometry("600x400")
        self.create_nav_bar()
        self.pages = {}
        self.create_pages()
        self.show_page("CalorieCounter")

    def create_nav_bar(self):
        nav_frame = tk.Frame(self, height=40, bg='grey')
        nav_frame.pack(side="top", fill="x")
        tk.Button(nav_frame, text="Calorie Counter", command=lambda: self.show_page("CalorieCounter")).pack(side="left", fill="both", expand=1)
        tk.Button(nav_frame, text="Practice", command=lambda: self.show_page("Practice")).pack(side="left", fill="both", expand=1)
        tk.Button(nav_frame, text="Stats", command=lambda: self.show_page("Stats")).pack(side="left", fill="both", expand=1)

    def create_pages(self):
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # Initialize CalorieCounter and Stats without user_id
        for F in (CalorieCounter, Stats):
            page = F(container)
            self.pages[F.__name__] = page.frame
            page.frame.grid(row=0, column=0, sticky="nsew")

        # Initialize Practice with user_id
        practice_page = Practice(container, user_id=self.user_id)
        self.pages["Practice"] = practice_page.frame
        practice_page.frame.grid(row=0, column=0, sticky="nsew")

    def show_page(self, page_name):
        frame = self.pages[page_name]
        frame.tkraise()

if __name__ == "__main__":
    # Example user_id for testing
    app = Boxing_App(user_id=1)
    app.mainloop()
