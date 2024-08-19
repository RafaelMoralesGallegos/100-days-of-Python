import random
import turtle as t
from turtle import Screen, Turtle

tim = Turtle()
tim.shape("turtle")
t.colormode(255)


def change_color():
    R = random.randint(0, 255)
    B = random.randint(0, 255)
    G = random.randint(0, 255)

    tim.color(R, G, B)


# * For a Square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)


# * For Dashed Line
# for _ in range(15):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()

# * For Square and other figures
# sides = 3
# for _ in range(8):
#     for _ in range(sides):
#         tim.forward(100)
#         angle = 360/sides
#         tim.right(angle)
#     change_color()
#     sides += 1

# *For a Random Walk
# tim.width(5)
# tim.speed("fastest")
# angle = [0, 90, 180, 270]
# for _ in range(300):
#     change_color()
#     tim.forward(20)
#     tim.right(random.choice(angle))

# * Drawing a Circle
degree = 0
tim.speed("fastest")


def draw_spirograh(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        change_color()
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograh(5)

#! This Most Be at the bottom of the code
screen = Screen()
screen.exitonclick()
