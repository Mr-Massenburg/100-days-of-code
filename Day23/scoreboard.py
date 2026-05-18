from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.setpos(-280, 250)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def update_level(self):
        self.level += 1

    def game_over(self):
        self.setpos(0,0)
        self.write("GAME OVER", align="center", font=FONT)

