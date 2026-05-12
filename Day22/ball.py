from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setheading(45)
        self.move_speed = 0.1


    def ball_move(self):
        self.forward(10)

    def bounce(self):
        self.setheading(-self.heading())

    def bounce_paddle(self):
        self.setheading(180 - self.heading())
        self.move_speed *= .9

    def reset_game(self):
        serve = self.xcor()

        self.setposition(0, 0)
        self.move_speed = 0.1

        if serve > 0:
            self.setheading(135)
        else:
            self.setheading(45)
