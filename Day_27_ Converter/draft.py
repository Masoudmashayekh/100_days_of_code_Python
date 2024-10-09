from tkinter import *


def button_clicked():
    my_label["text"] = entry.get()


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

# Label
my_label = Label(text="I am a Label", font=("Arial", 20, "bold"))
# my_label.pack(side="top")
my_label.grid(column=0, row=0)
# my_label["text"] = "New text 1"
# OR
# my_label.config(text="")
my_label.config(padx=20, pady=20)

# Buttons
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

button_2 = Button(text="Click Me", command=button_clicked)
# button.pack()
button_2.grid(column=2, row=0)
# Entry
entry = Entry(width=10)
entry.grid(column=3, row=3)

window.mainloop()


# -------------------
def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(5, add=5, multiply=5)


# --------------------------

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")


my_car = Car(make="Nissan")
print(my_car.make)
print(my_car.model)
