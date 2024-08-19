from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.setheading(45)
        self.prev_position = (self.pos())
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.ball_speed *= 0.8
        self.x_move *= -1

    def point(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.x_move *= -1
