# Day 22 | Pong 

from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)

scoreboard = Scoreboard()
player_1 = Paddle(350)
player_2 = Paddle(-350)

ball = Ball()

screen.listen()
screen.onkey(player_1.move_up, "Up")
screen.onkey(player_1.move_down, "Down")

screen.onkey(player_2.move_up, "w")
screen.onkey(player_2.move_down, "s")

game_is_running = True
while game_is_running:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(player_1) < 50 and ball.xcor() > 320 or ball.distance(player_2) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    if ball.xcor() > 400:
        scoreboard.update_score_l()
        ball.reset_game()


    if ball.xcor() < -400:
        scoreboard.update_score_r()
        ball.reset_game()


screen.exitonclick()
