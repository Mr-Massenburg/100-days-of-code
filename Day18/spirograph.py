# Coding Challenge - To get prepared for the final project, worked on creating a spirograph using Turtle graphics

import random
from turtle import Turtle, Screen, colormode

def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim = Turtle()
colormode(255)
tim.speed("fastest")

radius = 100
gap = 5

for i in range(0, 360, gap):
    tim.color(get_random_color())
    tim.setheading(i)
    tim.circle(radius)

screen = Screen()
screen.exitonclick()
