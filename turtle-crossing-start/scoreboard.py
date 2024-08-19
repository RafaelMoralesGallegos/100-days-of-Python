from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.goto(-280, 260)
        self.color("black")
        self.hideturtle()
        self.speed("fastest")
        self.level = 1
        self.update_scoreboard()

    def increase_score(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align=ALIGMENT, font=FONT)
