from turtle import Turtle

START_POS = [(0, 0), (-10, 0), (-20, 0)]
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START_POS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            position = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(position)
        self.head.forward(10)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        new_square = Turtle(shape="square")
        new_square.shapesize(stretch_len=0.5, stretch_wid=0.5)
        new_square.color("green")
        new_square.pu()
        new_square.goto(position)
        self.segments.append(new_square)

    def reset(self):
        for segments in self.segments:
            segments.goto(1000, 1000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
