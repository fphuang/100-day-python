import turtle as t
import random
import colorgram

t.colormode(255)
screen = t.Screen()
screen_width = 800
screen_height = 600
screen.setup(width=screen_width, height=screen_height)


def get_turtle_colors():
    return ["red", "orange", "yellow", "green", "blue", "purple"]


def create_turtles():
    turtles = []
    colors = get_turtle_colors()
    cor_y_init = -screen_height//2 + 100
    for index in range(0, len(colors)):
        turtle = t.Turtle(shape="turtle")
        turtle.turtlesize(2, 2)
        turtle.color(colors[index])
        turtle.penup()
        turtle.goto(-screen_width//2 + 20, cor_y_init + (index + 1) * 60)
        turtles.append(turtle)
    return turtles


def get_use_bet():
    return screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


def race(turtle_list, target):
    winners = []
    while True:
        for turtle in turtle_list:
            turtle.forward(random.randint(1, 10))
            if turtle.xcor() >= target:
                winners.append(turtle.pencolor())

        if len(winners) > 0:
            break

    return winners


user_bet = get_use_bet()
winners = race(create_turtles(), screen_width//2)
if user_bet in winners:
    print(f"You've won! The winner turtle is {user_bet}")
else:
    print(f"You've lost! The winner turtle is {winners}")

screen.exitonclick()
