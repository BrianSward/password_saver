# Imports
from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json


# Functions
def make_password():
    """Password Generator Project from earlier in course"""

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(7, 10)
    nr_symbols = random.randint(1, 3)
    nr_numbers = random.randint(3, 5)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    str_var = password_letters + password_numbers + password_symbols
    random.shuffle(str_var)
    pw = ''.join(str_var)
    password_e.insert(0, pw)
    pyperclip.copy(f"{pw}")


def save_function():
    """saves url, email/username, and pw to pw.json"""
    url = website_e.get()
    email = email_user_e.get()
    pw = password_e.get()
    new_data = {
        url: {
            "email": email,
            "password": pw,
        },
    }

    if len(url) > 0 and len(pw) > 0:

        is_ok = messagebox.askokcancel(title=f"Infor for {url}", message=f"User: {email}\nPassword: {pw}\nIf "
                                                                         f"this information is correct please "
                                                                         f"click 'Ok' to save.")
        if is_ok:
            try:
                with open("pw.json", mode="r") as file:
                    data = json.load(file)
                    data.update(new_data)

                with open("pw.json", mode="w") as file:
                    json.dump(data, file, indent=4)

            except FileNotFoundError:
                with open("pw.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)

            finally:
                website_e.delete(0, END)
                password_e.delete(0, END)

    else:
        messagebox.showinfo(title="Error Notice", message="Don't Leave Fields Blank!")


def search_for_data():
    search_term = website_e.get()
    try:
        with open("pw.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Database Error",
                            message="No Database exists yet! Please enter some passwords!")
    else:
        if search_term in data:
            messagebox.showinfo(title=f"{search_term} Information",
                                message=f"USERNAME: {data[search_term]['email']}\n"
                                        f"PASSWORD: {data[search_term]['password']}")
        else:
            messagebox.showinfo(title=f"{search_term} Information",
                                message=f"No information for {search_term} exists!")


# UI/Tkinter Config
window = Tk()

window.title("Password Manager")
window.config(bg="white", padx=20, pady=20, width=200, height=200)

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_l = Label(text="Website:  ", bg="white", highlightthickness=0)
website_l.grid(column=0, row=1, sticky="E")
website_e = Entry(width=30)
website_e.grid(column=1, row=1, columnspan=1, sticky="W")
website_e.focus()
website_b = Button(text="Search For PW", command=search_for_data)
website_b.grid(column=2, row=1, sticky="E")

email_user_l = Label(text="Email/Username:  ", bg="white", highlightthickness=0)
email_user_l.grid(column=0, row=2, sticky="E")
email_user_e = Entry(width=55)
email_user_e.grid(column=1, row=2, columnspan=2, sticky="W")
email_user_e.insert(0, "email@email.com")

password_l = Label(text="Password:  ", bg="white", highlightthickness=0)
password_l.grid(column=0, row=3, sticky="E")
password_e = Entry(width=30)
password_e.grid(column=1, row=3, sticky="W")
password_b = Button(text="Generate Password!", command=make_password)
password_b.grid(column=2, row=3, sticky="E")

add_button = Button(text="Add", command=save_function)
add_button.grid(column=1, row=4, columnspan=2, sticky="W")

window.mainloop()
