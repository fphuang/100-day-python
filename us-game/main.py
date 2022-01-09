import turtle
from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                    prompt="What's another state's name").title()
    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states]

        df = pd.DataFrame(missing_states)
        df.to_csv("missing_states.txt")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()


