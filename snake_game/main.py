import time
from turtle import Screen

from edge import Edge
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

edge = Edge((600, 600))
food = Food()
snake = Snake()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

time_score = scoreboard.score
speed = 0.1

game_on = True

while game_on:
    screen.update()

    # * Modifing In Game Speed
    if scoreboard.score == time_score + 10 and speed > 0.05:
        speed -= 0.01
        time_score = scoreboard.score

    time.sleep(speed)

    snake.move()

    # * Detect colition with food
    if snake.head.distance(food) < 12:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # * Detect collision with wall.
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        scoreboard.reset()
        snake.reset()

    # * Detect collision with self.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()
