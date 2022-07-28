from turtle import Turtle, Screen

import pandas

turtle = Turtle()
screen = Screen()
img = "blank_states_img.gif"

screen.title("Guess The State or Enter Exit")

screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
state_list = list(data["state"])

guess_state = []


while len(guess_state) < len(state_list):
    user_answer = screen.textinput(title=f"{len(guess_state)}/{len(state_list)} State Correct", prompt="Guess the State or Enter Exit").title()

    if user_answer == 'Exit':
        learn_it = [state for state in state_list if state not in guess_state]

        data_new = pandas.DataFrame(learn_it)
        data_new.to_csv("learn.csv")
        break

    elif user_answer in state_list:
        tim = Turtle()
        tim.penup()
        tim.hideturtle()
        coordinate = data[data["state"] == user_answer]
        tim.goto(int(coordinate.x), int(coordinate.y))
        tim.write(user_answer)
        guess_state.append(user_answer)



