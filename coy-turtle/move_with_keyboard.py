import turtle as t
import random
import colorgram

t.colormode(255)
tim = t.Turtle()
tim.shape('turtle')
tim.speed('fastest')
screen = t.Screen()
tim.pendown()


def move_forwards():
    tim.forward(40)


def move_backwards():
    tim.back(40)


def turn_left():
    tim.setheading(tim.heading() + 10)


def turn_right():
    tim.setheading(tim.heading() - 10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "h")

screen.exitonclick()
