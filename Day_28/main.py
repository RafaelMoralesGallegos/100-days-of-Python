import math
from tkinter import *

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
my_timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_lable.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    match reps:
        case 1 | 3 | 5 | 7:
            count_down(work_sec)  # G
            title_label.config(text="Work", fg=GREEN)
        case 2 | 4 | 6:
            count_down(short_break_sec)  # P
            title_label.config(text="Break", fg=PINK)
        case 8:
            count_down(long_break_sec)  # R
            title_label.config(text="Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):  #

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_text = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            check_text += check_mark
        check_lable.config(text=check_text)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodore")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(
    window, text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold")
)
title_label.grid(row=0, column=1, sticky="nsew")

canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=r"Day_28\tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(row=1, column=1, sticky="nsew")

start_button = Button(window, text="Start", width=10, command=start_timer)
start_button.grid(row=2, column=0, sticky="e")

reset_button = Button(window, text="Reset", width=10, command=reset_timer)
reset_button.grid(row=2, column=2, sticky="w")

check_mark = "✔"

check_lable = Label(
    window,
    justify="center",
    anchor="center",
    fg=GREEN,
    bg=YELLOW,
    font=20,
)
check_lable.grid(row=3, column=1)

window.mainloop()
