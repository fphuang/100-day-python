import turtle as t
import random
import colorgram

t.colormode(255)
tim = t.Turtle()
tim.shape('turtle')
tim.speed('fastest')
screen = t.Screen()
directions = [0, 90, 180, 270]

colors = [(212, 154, 98), (242, 249, 247), (236, 241, 245),
          (53, 107, 131), (199, 142, 34), (178, 78, 33), (116, 156, 171),
          (124, 79, 98), (123, 175, 157), (226, 198, 129), (190, 88, 109),
          (12, 49, 64), (56, 39, 19), (40, 168, 128), (50, 126, 121), (199, 123, 143),
          (166, 21, 30), (225, 93, 78), (244, 163, 160), (38, 32, 34), (3, 25, 25),
          (79, 147, 169), (163, 26, 21), (19, 79, 91), (235, 166, 170), (171, 207, 190),
          (102, 127, 158), (163, 203, 211)]


def extract_colors():
    temp = colorgram.extract("spot-painting.jpg", 30)
    return [(color.rgb.r, color.rgb.g, color.rgb.b) for color in temp]


def paint_dots(rows, cols, step_width=40):
    for _ in range(0, rows):
        for _ in range(0, cols):
            tim.dot(20, random.choice(colors))
            tim.forward(step_width)
        tim.setheading(90)
        tim.forward(step_width)
        tim.setheading(180)
        tim.forward(step_width * cols)
        tim.setheading(0)


tim.penup()
tim.hideturtle()
paint_dots(10, 10)
screen.exitonclick()
