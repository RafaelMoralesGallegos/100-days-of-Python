import json
import random
from tkinter import *
from tkinter import messagebox

import pyperclip
from letters import letters

GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
PINK = "#e2979c"

# *---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = letters
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


def generate_password(entry_password):

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    entry_password.set(password)
    pyperclip.copy(password)


# *---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file(website, username, password):

    if website.get() == "" or password.get() == "":
        messagebox.showerror(
            title="Empty Entrys", message="Some Entry doesn't have any data"
        )
    else:
        new_data = {
            website.get(): {"email": username.get(), "password": password.get()}
        }
        try:
            with open(r"Day_29\data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data

        with open(r"Day_29\data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

        clear_entrys(website, username, password)


def clear_entrys(website, username, password):
    website.set("")
    username.set("rafamoralesg25@gmail.com")
    password.set("")


# *------------------------- SEARCH PASSWORD ---------------------------- #


def search_webiste(website):
    try:
        with open(r"Day_29\data.json", "r") as data_file:
            data = json.load(data_file)

        website_data = data[website.get()]
    except FileNotFoundError as error_message:
        messagebox.showerror(title=error_message, message="No Passwords created")
    except KeyError as error_message:
        messagebox.showerror(
            title=error_message, message="Webiste has no Password saved"
        )
    else:
        messagebox.showinfo(
            title=website.get(),
            message=(
                f"Email: {website_data["email"]}\n"
                f"Password: {website_data["password"]}"
            ),
        )


# *---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Variables
website = StringVar(window, "")
username = StringVar(window, "rafamoralesg25@gmail.com")
password = StringVar(window, "")

# Canvas
canvas = Canvas(window, width=200, height=200)
lock_img = PhotoImage(file=r"Day_29\logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1, sticky="nsew")

# Labels
website_label = Label(window, text="Website: ")
website_label.grid(row=1, column=0, padx=(0, 5))
username_label = Label(window, text="Email/Username: ")
username_label.grid(row=2, column=0, padx=(0, 5))
password_label = Label(window, text="Password: ")
password_label.grid(row=3, column=0, padx=(0, 5))

# Entry
website_entry = Entry(window, textvariable=website)
website_entry.grid(row=1, column=1, pady=5, padx=(0, 10), sticky="nsew")
website_entry.focus()
username_entry = Entry(window, textvariable=username)
username_entry.grid(row=2, column=1, columnspan=2, pady=5, sticky="nsew")
password_entry = Entry(window, width=21, textvariable=password)
password_entry.grid(row=3, column=1, pady=5, padx=(0, 10), sticky="nsew")

# Button
password_button = Button(
    window,
    text="Generate Password",
    bg=YELLOW,
    command=lambda: generate_password(password),
)
password_button.grid(row=3, column=2, sticky="ew")
add_button = Button(
    window,
    text="Add",
    bg=GREEN,
    command=lambda: save_to_file(website, username, password),
)
add_button.grid(row=4, column=1, columnspan=2, pady=5, sticky="ew")
search_button = Button(
    window, text="Search", bg=PINK, command=lambda: search_webiste(website)
)
search_button.grid(row=1, column=2, sticky="nsew")

window.mainloop()
