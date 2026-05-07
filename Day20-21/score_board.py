from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.setpos(0, 260)
        self.hideturtle()
        self.score = 0
        self.print_scoreboard()

    def print_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.print_scoreboard()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

