# Day 23 | Capstone Project Turtle Crossing Game

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tmnt = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(tmnt.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.make_car()
    car_manager.move_car()

    if tmnt.cross_finish_line():
        tmnt.level_complete()
        scoreboard.update_level()
        car_manager.increase_speed()
        scoreboard.show_score()

    for car in car_manager.cars:
        if tmnt.distance(car) <= 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
