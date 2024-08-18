import tkinter as tk
from calorie_counter import CalorieCounter
from practice import Practice
from stats import Stats
from PIL import Image, ImageTk

# Main Application Class
class Boxing_App(tk.Tk):
    def __init__(self, user_id, app_name="Boxing App"):
        super().__init__()
        self.user_id = user_id  # User ID for identifying the user
        self.app_name = app_name  # Application name
        self.setup()  # Call setup method to initialize the UI

    def setup(self):
        self.title(self.app_name)  # Set the window title
        self.geometry("375x500")  # Set the window size
        self.create_nav_bar()  # Create the navigation bar
        self.pages = {}  # Dictionary to store page frames
        self.create_pages()  # Create the pages
        self.show_page("CalorieCounter")  # Show the Calorie Counter page by default

    def create_nav_bar(self):
        # Create a navigation bar frame
        nav_frame = tk.Frame(self, height=40, bg='grey')
        nav_frame.pack(side="top", fill="x")

        # Add buttons to the navigation bar
        tk.Button(nav_frame, text="Calorie Counter", command=lambda: self.show_page("CalorieCounter")).pack(side="left", fill="both", expand=1)
        tk.Button(nav_frame, text="Practice", command=lambda: self.show_page("Practice")).pack(side="left", fill="both", expand=1)
        tk.Button(nav_frame, text="Stats", command=lambda: self.show_page("Stats")).pack(side="left", fill="both", expand=1)

        # Load and resize the logo image
        logo_image = Image.open("/Users/veerparmar/PycharmProjects/13DDT_Boxing/pngimg.com - boxing_gloves_PNG102613.png")
        logo_image = logo_image.resize((25, 20), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(logo_image)

        # Display the logo
        logo_label = tk.Label(nav_frame, image=self.logo, bg='grey')
        logo_label.pack(side="right", padx=10, pady=5)

    def create_pages(self):
        # Create a container frame to hold all pages
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # Instantiate and store each page
        for F in (CalorieCounter, Practice, Stats):
            page = F(container, user_id=self.user_id)  # Pass the container and user_id to the page class
            self.pages[F.__name__] = page.frame  # Store the frame in the pages dictionary
            page.frame.grid(row=0, column=0, sticky="nsew")  # Use grid layout manager to stack frames

    def show_page(self, page_name):
        # Bring the specified page to the front
        frame = self.pages[page_name]
        frame.tkraise()

# Run the application
if __name__ == "__main__":
    app = Boxing_App(user_id=1)  # For testing purposes, replace with actual user_id
    app.mainloop()
