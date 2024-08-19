from turtle import Turtle


class Ball_Net(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.pu()
        self.goto(0, 300)
        self.speed("fastest")
        self.create_net()

    def create_net(self):
        self.setheading(270)
        while self.ycor() > -300:
            self.pd()
            self.forward(20)
            self.pu()
            self.forward(20)
