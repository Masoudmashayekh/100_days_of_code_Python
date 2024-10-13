from tkinter import *
from tkinter import messagebox
import random
import pyperclip

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

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    [password_list.append(random.choice(letters)) for _ in range(nr_letters)]
    [password_list.append(random.choice(symbols)) for _ in range(nr_symbols)]
    [password_list.append(random.choice(numbers)) for _ in range(nr_numbers)]
    random.shuffle(password_list)

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
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \nEmail: {email}"
                                                              f" \nPassword: {password} \n Is it ok to save?")
        if is_ok:
            with open("Data.txt", mode="a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


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

website_entry = Entry(width=36)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky="nsew")

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

window.mainloop()
