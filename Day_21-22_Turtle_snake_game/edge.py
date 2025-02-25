from turtle import Turtle


class Edge(Turtle):
    def __init__(self, screensize) -> None:
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.pu()
        self.speed("fastest")
        self.screensize = screensize
        self.setheading(180)
        self.paint_margin()

    def paint_margin(self):
        half_cor = (self.screensize[0] / 2) - 20
        self.goto(-half_cor, half_cor)
        self.pd()
        for _ in range(0, 4):
            self.left(90)
            self.forward(self.screensize[0])
