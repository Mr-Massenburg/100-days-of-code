# Day 25 | US States Game - Using pandas, dataframes, series, and reading from CSV files. 

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

game_is_running = True
score = 0
correct_guesses = []

while game_is_running:
    answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")

    if answer is None or answer.lower() == "exit":
        game_is_running = False
        missed_states = []
        heading = "States To Study"
        for state in states:
            if state not in correct_guesses:
                missed_states.append(state)

        df = pandas.DataFrame({heading: missed_states})
        df.to_csv("states_to_learn.csv")
        break

    answer = answer.title()

    if answer in states and answer not in correct_guesses:
        x = data[data.state == answer]["x"].item()
        y = data[data.state == answer]["y"].item()
        state_text = turtle.Turtle()
        state_text.penup()
        state_text.hideturtle()
        state_text.setpos(x, y)
        state_text.write(f"{answer}")

        correct_guesses.append(answer)

        score += 1
    if score == 50:
        game_is_running = False
        break



