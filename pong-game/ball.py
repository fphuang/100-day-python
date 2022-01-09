from turtle import Turtle
import random

INITIAL_MOVE_SPEED = 0.1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.setposition(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = INITIAL_MOVE_SPEED

    def move(self):
        self.setposition(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move = -self.y_move

    def bounce_x(self):
        self.x_move = -self.x_move
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = INITIAL_MOVE_SPEED
        self.bounce_x()
