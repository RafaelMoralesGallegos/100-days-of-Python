import random
from tkinter import *

import pandas as pd

# *Data Base
try:
    data = pd.read_csv(r"data\words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv(r"data\french_words.csv")

to_learn = pd.DataFrame.to_dict(data, orient="records")
current_card = {}


# *Flip Cards
def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")

    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    df = pd.DataFrame(to_learn)
    df.to_csv(r"data\words_to_learn.csv", index=False)

    next_card()


# *UI
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.resizable(False, False)

flip_timer = window.after(3000, flip_card)

# Canvas
card_front_img = PhotoImage(file=r"images\card_front.png")
card_back_img = PhotoImage(file=r"images\card_back.png")

canvas = Canvas(
    window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0
)
canvas_img = canvas.create_image(400, 263, image=card_front_img)

canvas.grid(row=0, column=0, sticky="nsew", columnspan=2)
language_text = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))

# Buttons
right_img = PhotoImage(file=r"images\right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file=r"images\wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

#! This is last
next_card()
window.mainloop()
