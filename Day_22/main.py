from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from ball_net import Ball_Net
import time

# * Create the Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

scoreboard = Scoreboard()
ball_net = Ball_Net()

# * Create the Play Paddle
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

# * Game Actions
screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()

    # * Collision with Top and Bottom walls
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce()

    # * Collision with Paddle
    if (
        ball.xcor() > 320
        and ball.distance(r_paddle) < 50
        or ball.xcor() < -320
        and ball.distance(l_paddle) < 50
    ):
        ball.hit()

    # * Scored Point L_paddle
    if ball.xcor() > 380:
        ball.point()
        scoreboard.l_point()

    # * Scored Point R_paddle
    if ball.xcor() < -380:
        ball.point()
        scoreboard.r_point()

#! Do not Modify and keep at the End of Code.
screen.exitonclick()
