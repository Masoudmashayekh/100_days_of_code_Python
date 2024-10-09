from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=30)
window.minsize(width=300, height=200)
# Entry
entry = Entry(width=5, font=("Arial", 20))
num = entry.get()
entry.grid(row=0, column=1)


def miles_to_km():
    miles = float(entry.get())
    km = miles * 1.60934
    answer.config(text=f"{km}")


# Label 1
miles_label = Label(text="Miles", font=("Arial", 20))
miles_label.grid(row=0, column=2)

# Label 2
is_equal_to = Label(text="is equal to", font=("Arial", 15))
is_equal_to.grid(row=1, column=0)

# Label 3
answer = Label(text="0", font=("Arial", 20, "bold"))
answer.grid(row=1, column=1)
answer.config(padx=5, pady=5)

# Label 4
km_label = Label(text="Km", font=("Arial", 20))
km_label.grid(row=1, column=2)

# Button
button = Button(text="Calculate", font=("Arial", 15), command=miles_to_km)
button.grid(row=2, column=1)
button.config(padx=5, pady=5)

window.mainloop()
