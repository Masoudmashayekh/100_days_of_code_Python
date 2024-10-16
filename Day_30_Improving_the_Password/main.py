from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

LABEL_FONT = ("Arial", 10)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []
    [password_list.append(choice(letters)) for _ in range(nr_letters)]
    [password_list.append(choice(symbols)) for _ in range(nr_symbols)]
    [password_list.append(choice(numbers)) for _ in range(nr_numbers)]
    shuffle(password_list)

    password_r = "".join(password_list)

    # password_r = ""
    # for char in password_list:
    #     password_r += char

    password_entry.delete(0, END)
    password_entry.insert(0, password_r)
    pyperclip.copy(password_r)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website.title(): {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                try:
                    data = json.load(data_file)
                except json.JSONDecodeError:
                    data = {}
                    # with open("data.json", "w") as data_file:
                    #     json.dump(new_data, data_file, indent=4)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            try:
                data = json.load(data_file)
            except json.JSONDecodeError:
                data = {}
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        web_t = website.title()
        if web_t in data:
            email = data[web_t]["email"]
            password = data[web_t]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels -----------------------------------------------------------------
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="w")

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0, sticky="w")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="w")

# Entries -----------------------------------------------------------------

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1, sticky="nsew")

username_entry = Entry(width=36)
username_entry.grid(row=2, column=1, columnspan=2, sticky="nsew")
username_entry.insert(0, "masoud@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="nsew")

# Button ---------------------------------------------------------------
generate_button = Button(text="Generate Password", command=pass_generator)
generate_button.grid(row=3, column=2, sticky="nsew")

add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2, sticky="nsew")

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="nsew")

window.mainloop()
