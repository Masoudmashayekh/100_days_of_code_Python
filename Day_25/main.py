from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle = Turtle()
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
data_dict = data.to_dict()
state_lists = data["state"].to_list()

guessed_states = []
while len(guessed_states) < len(state_lists):
    answer_state = screen.textinput(f"Guess the State {len(guessed_states)} / {len(state_lists)}",
                                    "What's another state's name?").title()

    if answer_state == "Exit":
        break

    if answer_state in state_lists:
        guessed_states.append(answer_state)
        state_turtle = Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_data = data[data.state == answer_state]
        state_turtle.goto(state_data.x.item(), state_data.y.item())
        state_turtle.write(answer_state)
missing_state = []
for state in state_lists:
    if state not in guessed_states:
        missing_state.append(state)
new_data = pandas.DataFrame(missing_state)
new_data.to_csv("state_to_learn.csv")
