from tkinter import *
from tkinter import messagebox
from boxing_app import Boxing_App  # Ensure this import is correct
from database import verify_user, get_user_id  # Import the verify_user and get_user_id functions

# Function to handle the login process
def Ok():
    uname = e1.get()  # Get the entered username
    password = e2.get()  # Get the entered password

    if uname == "" and password == "":
        # Show a message box if both fields are blank
        messagebox.showinfo("", "Blank Not allowed")
    elif verify_user(uname, password):
        # Verify the username and password
        user_id = get_user_id(uname)  # Get the user ID associated with the username
        messagebox.showinfo("", "Login Success")
        root.destroy()  # Close the login window
        app = Boxing_App(user_id=user_id)  # Launch the main application with the user_id
        app.mainloop()  # Start the main application's event loop
    else:
        # Show a message box if the username or password is incorrect
        messagebox.showinfo("", "Incorrect Username and Password")

# Create the main login window
root = Tk()
root.title("Login")  # Set the window title
root.geometry("300x200")  # Set the window size

# Create and place labels for username and password
Label(root, text="UserName").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)

# Create and place entry fields for username and password
e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")  # Hide the password input

# Create and place the login button
Button(root, text="Login", command=Ok, height=3, width=13).place(x=10, y=100)

# Start the Tkinter event loop
root.mainloop()
