import turtle as t
import random

# colors = clr.extract(
#     'D:/Documentos/Python/100 days of Python/Day_18/image.jpg', 2**32)
# color_palette = []

# for i in range(len(colors)):
#     color = colors[i]
#     color_red = color.rgb.r
#     color_green = color.rgb.g
#     color
#     new_color = (color_red, color_green, color_blue)
#     color_palette.append(new_color)

# print(color_palette)

color_palette = [
    (42, 104, 172),
    (234, 206, 114),
    (228, 151, 85),
    (187, 47, 75),
    (118, 88, 47),
    (231, 117, 145),
    (111, 108, 188),
    (215, 60, 78),
    (54, 178, 111),
    (114, 185, 137),
    (120, 177, 214),
    (200, 17, 41),
    (115, 170, 35),
    (33, 57, 112),
    (221, 53, 47),
    (25, 142, 108),
    (181, 168, 224),
    (155, 224, 193),
    (28, 163, 174),
    (85, 35, 39),
    (32, 45, 83),
    (232, 167, 181),
    (77, 36, 34),
    (234, 171, 162),
    (111, 43, 38),
    (152, 208, 221),
    (70, 74, 46),
    (12, 77, 104),
    (5, 115, 82),
]

t.colormode(255)
tim = t.Turtle()

# * We begin
tim.penup()
x = -250
y = -250
tim.goto(x, y)

for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_palette))
        tim.penup
        tim.forward(50)
    y += 50
    tim.penup()
    tim.goto(x, y)


#! This Most Be at the bottom of the code
screen = t.Screen()
screen.exitonclick()
