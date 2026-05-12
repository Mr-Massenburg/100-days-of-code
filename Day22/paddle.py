from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_start):
        super().__init__()
        self.x_start = x_start
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.resizemode("user")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.setx(self.x_start)
        self.color("white")

    def move_up(self):
        if self.ycor() < 250:
            self.forward(20)

    def move_down(self):
        if self.ycor() > -250:
            self.backward(20)
