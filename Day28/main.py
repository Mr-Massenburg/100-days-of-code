# Day 28 | Pomodoro Timer App using Tkinter - Introduction to Canvas in Tkinter

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

# -------------------------- GLOBAL VARIABLES ---------------------------- #

reps = 0
text = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global text
    global reps
    text = ""
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_display, text="00:00")
    progress_label.config(text=text)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
    elif reps % 2 == 0 and reps % 8 != 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps
    global text
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_display, text=f"{count_min}:{count_sec:02}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 != 0:
            text += "✔"
            progress_label.config(text=text)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
background_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=background_img)
timer_display = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

progress_label = Label(bg=YELLOW, fg=GREEN)
progress_label.grid(column=1, row=3)



window.mainloop()
