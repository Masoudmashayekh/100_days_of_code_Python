from tkinter import *
import random
import pandas

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_NAME_FONT = ("Arial", 40, "italic")
ANSWER_FONT = ("Arial", 60, "bold")
# ---------------------------- Data ----------------------------------- #
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/Italian_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language_name_text, text="Italian", fill="black")
    canvas.itemconfig(answer_text, text=current_card["Italian"], fill="black")
    canvas.itemconfig(card_image, image=front_image)
    flip_timer = window.after(3000, func=flip_card)


def known_card():
    to_learn.remove(current_card)
    print(len(to_learn))
    data_ = pandas.DataFrame(to_learn)
    data_.to_csv("data/word_to_learn.csv", index=False)
    next_card()


def flip_card():
    canvas.itemconfig(language_name_text, text="English", fill="white")
    canvas.itemconfig(answer_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_image, image=back_image)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=525)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=front_image)
language_name_text = canvas.create_text(400, 150, text="Title", font=LANGUAGE_NAME_FONT)
answer_text = canvas.create_text(400, 300, text="Word", font=ANSWER_FONT)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Button ----------------------------------------------------------------------
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_image, highlightthickness=0, command=known_card)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1, pady=20)
wrong_button.grid(row=1, column=0, pady=20)

next_card()

window.mainloop()
