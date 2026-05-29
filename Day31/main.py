# Day 31 | Capstone Project - Flash Card program. Using all Tkinter knowledge and Pandas

from tkinter import *
import pandas
import random

current_pair ={}
BACKGROUND_COLOR = "#B1DDC6"

# -------------------------- DATA  ---------------------------#
try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")

data = df.to_dict(orient="records")


# -------------------------- NEW WORD ---------------------------#
def new_word():
    global current_pair
    global timer

    window.after_cancel(timer)
    current_pair = random.choice(data)

    card_canvas.itemconfig(card_graphic, image=card_front_image)
    card_canvas.itemconfig(language, text="French", fill="black")
    card_canvas.itemconfig(word, text=current_pair["French"], fill="black")
    timer = window.after(3000, flip_card)


# -------------------------- FLIP CARD ---------------------------#
def flip_card():
    card_canvas.itemconfig(card_graphic, image=card_back_image)
    card_canvas.itemconfig(language, text="English", fill="white")
    card_canvas.itemconfig(word, text=current_pair["English"], fill="white")

# -------------------------- REMOVE FROM LIST ---------------------------#
def remove_known_words():
    data.remove(current_pair)
    new_data = pandas.DataFrame(data)
    new_data.to_csv("data/words_to_learn.csv", index=False)

# -------------------------- RIGHT ANSWER ---------------------------#
def right_answer():
    remove_known_words()
    new_word()

# ------------------ UI SETUP --------------------- #

# MAIN WINDOW
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

timer = window.after(3000, flip_card)


# IMAGE SOURCES
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")

right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")

# CARD SETUP
card_canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_graphic = card_canvas.create_image(400, 263, image=card_front_image)
card_canvas.grid(column=0, row=0, columnspan=2)
language = card_canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))
word = card_canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))

# BUTTON SETUP
wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=new_word)
wrong_button.grid(column=0, row=1)

right_button = Button(image=right_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=right_answer)
right_button.grid(column=1, row=1)

new_word()

window.mainloop()
