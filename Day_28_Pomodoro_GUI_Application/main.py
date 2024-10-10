from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = "None"


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(time_text, text="00:00")
    marks_label.config(text="")
    timer_label.config(text="Timer")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_time()
        work_sessions = math.floor(reps / 2)
        marks = ""
        for _ in range(work_sessions):
            marks += "✓"
        marks_label.config(text=marks, fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=200, pady=200, bg=YELLOW)

# Label 1
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(row=0, column=1)

# Label 2
marks_label = Label(bg=YELLOW, font=(FONT_NAME, 25, "bold"))
marks_label.config(padx=20, pady=20)
marks_label.grid(row=2, column=1)

# Button 1
start_button = Button(text="Start", command=start_time, bg=YELLOW, font=(FONT_NAME, 15, "bold"), highlightthickness=0)
start_button.grid(row=2, column=0)

# Button 2
Reset_button = Button(text="Reset", command=reset_timer, bg=YELLOW, font=(FONT_NAME, 15, "bold"), highlightthickness=0)
Reset_button.grid(row=2, column=2)

canvas = Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
time_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

window.mainloop()
