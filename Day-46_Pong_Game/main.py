from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

# Screen Setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detecting collision between ball and wall
    if ball.xcor() > 280 or ball.ycor() < -280:
        # Ball gets bouncing
        ball.bounce_y()

    # Detecting collision between paddles and the ball
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() > -320
    ):
        ball.bounce_x()

screen.exitonclick()
