import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = (
        screen.textinput(
            title=f"{len(guessed_states)}/50", prompt="What is another state?"
        )
        .title()
        .strip()
    )
    guessed_states.append(answer_state)

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        df = pd.DataFrame(missing_states)
        df.to_csv("missing_states.csv")
        exit()

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
    else:
        print("Wrong!")
