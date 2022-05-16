from tkinter import *
from users.UserController import UserController

app = Tk()
app.title("Es app")
app.geometry("500x400")

frame = Frame(app)
frame.pack()
Label(frame, text="Email").pack()
email = Entry(frame)
email.pack()

Label(frame, text="Password").pack()
password = Entry(frame, show="*")
password.pack()

def home():
    frame.destroy()
    home_page = Frame(app)
    home_page.pack()
    Label(home_page, text="Home").pack()

def auth(doType: str = None):
    if email.get() and password.get():
        user_controller = UserController()
        data = {
            "email": email.get(),
            "password": password.get()
        }
        if doType == "registration":
            return user_controller.registration(data)

        if user_controller.login(data):
            app.after(10, lambda: home())


    return "Credentials error"


Button(frame, text="Login", command=lambda: auth()).pack()
Button(frame, text="Registration", command=lambda: auth('registration')).pack()

app.mainloop()
