import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    cars.move_cars()

    # Detect when the turtle player collides with a car and stop the game if this happens.
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y).
    # When this happens, return the turtle to the starting position and increase the speed of the cars.
    if player.is_turtle_finished():
        player.goto_start()
        cars.level_up()
        scoreboard.increase_level()


screen.exitonclick()
