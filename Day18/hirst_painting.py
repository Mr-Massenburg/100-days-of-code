# Day 18 | Hirst Painting Replication - Using additional classes and turtle graphics

# Class used to extract colors from an image. The extracted colors were assigned to color_list and used as the random colors in the final project
# import colorgram
#
# colors = colorgram.extract("lego_painting.jpg", 30)
# paint_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     paint_colors.append(new_color)
#
# print(paint_colors)

from turtle import Turtle, Screen, colormode
import random

tmnt = Turtle()
colormode(255)
tmnt.penup()
tmnt.hideturtle()
tmnt.speed("fastest")

color_list = [(16, 25, 34), (107, 94, 75), (47, 31, 23), (180, 163, 145), (28, 20, 23), (203, 219, 214), (224, 127, 148), (87, 96, 87), (29, 127, 168), (247, 193, 221), (2, 181, 219), (248, 160, 159), (146, 61, 73), (145, 165, 154), (32, 43, 31), (175, 166, 20), (236, 164, 193), (202, 209, 124), (201, 79, 90), (149, 22, 28), (83, 87, 17), (117, 182, 210), (107, 129, 151), (192, 95, 80), (125, 42, 25), (176, 197, 189), (192, 229, 235), (50, 75, 54), (139, 210, 227)]

# Setting position to try and center the final result on the screen
x = -225
y = -225

tmnt.setpos(x, y)

rows = 10
columns = 10

for _ in range(0, rows):
    for _ in range(0, columns):
        color = random.choice(color_list)
        tmnt.color(color)
        tmnt.dot(20)
        tmnt.forward(50)
    y += 50
    tmnt.setpos(x, y)

screen = Screen()
screen.exitonclick()
