# Day 28 | Miles to Km converter - Learning the basics of Tkinter and making GUIs

from tkinter import *

def calculate():
    miles = float(miles_input.get())
    km = miles * 1.609344
    km_result.config(text=f"{km:.2f}")

# ------------------- Window Setup -------------------
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# ------------------- UI Elements -------------------
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)
miles_input.focus()

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result = Label(text="0")
km_result.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)


window.mainloop()
