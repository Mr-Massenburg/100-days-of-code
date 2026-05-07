from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.snake_body = []
        self.make_snake()
        self.head = self.snake_body[0]

    def make_snake(self):
        for _ in range(3):
            position = (self.x, self.y)
            self.add_segment(position)
            self.x -= 20

    def add_segment(self, position):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.setpos(position)
        self.snake_body.append(snake)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())


    def move(self):
        for segment in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment - 1].xcor()
            new_y = self.snake_body[segment - 1].ycor()
            self.snake_body[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


