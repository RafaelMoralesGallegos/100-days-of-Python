import os
from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.score = 0
        self.current_dir = os.path.dirname(__file__)
        self.file_path = os.path.join(self.current_dir, "highscore.txt")
        with open(self.file_path, "r") as file:
            content = file.read()
            self.highscore = int(content)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(self.file_path, mode="w") as file:
                file.write(str(self.highscore))

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.highscore}",
            align=ALIGMENT,
            font=FONT,
        )
