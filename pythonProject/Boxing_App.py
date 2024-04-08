import tkinter as tk
from Calorie_Counter import CalorieCounter
from Practice import Practice
from Community_Forum import CommunityForum


# Main Application Class
class App(tk.Tk):
    def __init__(self, app_name="Boxing App"):
        super().__init__()
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
        tk.Button(nav_frame, text="Community", command=lambda: self.show_page("CommunityForum")).pack(side="left", fill="both", expand=1)

    def create_pages(self):
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        for F in (CalorieCounter, Practice, CommunityForum):
            page = F(container)
            self.pages[F.__name__] = page.frame
            page.frame.grid(row=0, column=0, sticky="nsew")

    def show_page(self, page_name):
        frame = self.pages[page_name]
        frame.tkraise()

# App Name Setting / Login Window
def show_app_name_setting_window():
    login_window = tk.Tk()
    login_window.title("Set App Name")

    tk.Label(login_window, text="Enter App Name:").pack()
    app_name_var = tk.StringVar()
    tk.Entry(login_window, textvariable=app_name_var).pack()

    def on_submit():
        app_name = app_name_var.get()
        login_window.destroy()  # Close the login window
        app = App(app_name)  # Start the main application with the specified app name
        app.mainloop()

    tk.Button(login_window, text="Submit", command=on_submit).pack()
    login_window.mainloop()

# Start the application
if __name__ == "__main__":
    show_app_name_setting_window()
