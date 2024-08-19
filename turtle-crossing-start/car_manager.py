from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.new_car()

    def new_car(self):
        newcar = Turtle()
        newcar.shape("square")
        newcar.pu()
        newcar.setheading(180)
        newcar.color(random.choice(COLORS))
        newcar.shapesize(stretch_len=2, stretch_wid=1)
        random_y = random.randint(-250, 250)
        newcar.goto(300, random_y)
        self.cars.append(newcar)

    def move(self):
        for items in self.cars:
            items.forward(self.speed)

    def car_control(self):
        for items in self.cars:
            position = items.xcor()
            if position < -300:
                items.clear()

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
