# Day 19 | Sketch with Turtle - More turtle graphics practice and event listeners

from turtle import Turtle, Screen

tmnt = Turtle()
screen = Screen()

tmnt.speed("fastest")

def move_forward():
    tmnt.forward(10)

def move_backward():
    tmnt.backward(10)

def tilt_left():
    tmnt.left(10)

def tilt_right():
    tmnt.right(10)

def clear():
    tmnt.reset()

screen.listen()

#WASD controls
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=tilt_left)
screen.onkey(key="d", fun=tilt_right)

#Arrow controls
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="Left", fun=tilt_left)
screen.onkey(key="Right", fun=tilt_right)

#Clearing/resetting screen
screen.onkey(key="c", fun=clear)

screen.exitonclick()
