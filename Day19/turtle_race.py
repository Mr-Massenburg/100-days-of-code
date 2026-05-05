# Day 19 | Turtle Race - Multiple object instances

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Place Your Bet!", "Which turtle will win the race? Enter a color:").lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []
race_is_happening = False

# Setting the starting position of the first turtle
x = -230
y = -100

# Creates a list of multiple instances of the turtle object
for color in colors:
    tmnt = Turtle("turtle")
    tmnt.color(color)
    tmnt.penup()
    tmnt.goto(x, y)
    all_turtles.append(tmnt)
    y += 40 #Shifting each turtle up to create the starting line of the race

# Validates user input
if user_bet in colors:
    race_is_happening = True
else:
    print(f"Invalid selection. Please choose from: {colors}")

while race_is_happening:
    for turtle in all_turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() >= 230: # Checks which turtle makes it to the end of the screen first
            winner = turtle.pencolor()
            race_is_happening = False
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
            break


screen.exitonclick()
