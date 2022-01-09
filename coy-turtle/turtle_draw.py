# from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)
timmy = t.Turtle()
timmy.shape('turtle')
timmy.speed('fastest')
screen = t.Screen()
directions = [0, 90, 180, 270]


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def draw_circle():
    for n in range(4):
        timmy.forward(100)
        timmy.left(90)


def draw_dash_line():
    for n in range(10):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()


def draw_shape_downward(sides_num, steps):
    for _ in range(sides_num):
        angel = 360/sides_num
        timmy.forward(steps)
        timmy.right(angel)


def draw_shape_upward(sides_num, steps):
    for _ in range(sides_num):
        angel = 360/sides_num
        timmy.forward(steps)
        timmy.left(angel)


def walk_random():
    timmy.color(random_color())
    timmy.pensize(10)
    timmy.forward(30)
    timmy.setheading(random.choice(directions))


def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

# for sides_num in range(3, 11):
#     timmy.color(colors[sides_num - 3])
#     draw_shape_downward(sides_num, 50)
#
# for sides_num in range(3, 11):
#     timmy.color(colors[sides_num - 3])
#     draw_shape_upward(sides_num, 50)

# for _ in range(200):
#     walk_random()


draw_spirograph(5)

screen.exitonclick()

