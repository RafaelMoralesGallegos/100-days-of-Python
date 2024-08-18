from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=290)

race_on = False

user_bet = screen.textinput(
    title="make your bet", prompt="Which turtle will win the race? Enter a color: "
)

y_positions = [-100, -60, -20, 20, 60, 100]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []

finish_line = Turtle()
finish_line.pu()
finish_line.goto(x=350, y=140)
finish_line.right(90)

while finish_line.ycor() > -140:
    finish_line.pd()
    finish_line.forward(20)
    finish_line.pu()
    finish_line.forward(20)
finish_line.hideturtle()

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.pu()
    new_turtle.goto(x=-350, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True
while race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= 350:
            race_on = False
            winner = turtle.pencolor()

if winner == user_bet:
    user_state = "win"
else:
    user_state = "lose"

print(f"You {user_state}. The winner was the {winner} turtle.")
screen.exitonclick()
