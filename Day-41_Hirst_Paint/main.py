from turtle import *
import turtle as tur
import random

tur.colormode(255)
tutu = tur.Turtle()
tutu.speed("fastest")
tutu.penup()
tutu.hideturtle()

color_list = [
    (187, 162, 20),
    (154, 80, 34),
    (243, 239, 242),
    (25, 85, 139),
    (24, 59, 125),
    (228, 127, 98),
    (26, 9, 5),
]

tutu.setheading(225)
tutu.forward(300)
tutu.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    tutu.dot(20, random.choice(color_list))
    tutu.forward(50)

    if dot_count % 10 == 0:
        tutu.setheading(90)
        tutu.forward(50)
        tutu.setheading(180)
        tutu.forward(500)
        tutu.setheading(0)

screen = tur.Screen()
screen.exitonclick()
