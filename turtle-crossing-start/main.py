import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# *Player Turtle
player = Player()
screen.listen()
screen.onkeypress(player.move, "Up")

# *Car Manager
cars = CarManager()
counter = 0

# * Scoreboard
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    counter += 1
    if counter == 6:
        cars.new_car()
        counter = 0

    cars.car_control()
    cars.move()

    # * Detect collision with Car.
    for car in cars.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # * Detect collision with Finifh Line.
    if player.ycor() > 275:
        player.finish_line()
        cars.increase_speed()
        scoreboard.increase_score()


#! DO NOT REMOVE
screen.exitonclick()
