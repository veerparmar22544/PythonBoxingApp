from tkinter import *
from tkinter import messagebox
from boxing_app import Boxing_App  # Ensure this import is correct
from database import verify_user, get_user_id  # Import the verify_user and get_user_id functions

def Ok():
    uname = e1.get()
    password = e2.get()

    if uname == "" and password == "":
        messagebox.showinfo("", "Blank Not allowed")
    elif verify_user(uname, password):
        user_id = get_user_id(uname)
        messagebox.showinfo("", "Login Success")
        root.destroy()  # Close the login window
        app = Boxing_App(user_id=user_id)  # Launch the main application with the user_id
        app.mainloop()  # Start the main application's event loop
    else:
        messagebox.showinfo("", "Incorrect Username and Password")

root = Tk()
root.title("Login")
root.geometry("300x200")

Label(root, text="UserName").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")

Button(root, text="Login", command=Ok, height=3, width=13).place(x=10, y=100)

root.mainloop()
