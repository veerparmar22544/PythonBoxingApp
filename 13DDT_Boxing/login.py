from tkinter import *
from tkinter import messagebox
from boxing_app import Boxing_App  # Import your main application class

def Ok():
    uname = e1.get()
    password = e2.get()

    if (uname == "" and password == ""):
        messagebox.showinfo("", "Blank Not allowed")

    elif (uname == "Admin" and password == "123"):
        messagebox.showinfo("", "Login Success")
        root.destroy()  # Close the login window
        app = Boxing_App()  # Launch the main application
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
