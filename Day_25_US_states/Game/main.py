import turtle

import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = r"Day_25\Game\blank_states_img.gif"
screen.addshape(image)

df = pd.read_csv(r"Day_25\Game\50_states.csv")
state_list = df.state.to_list()
total_answers = []

turtle.shape(image)
answer_turtle = turtle.Turtle(visible=False)
answer_turtle.up()


# 3. Write correct guess onto the map
# 3.1 Get turtle to Coordinates
def states_cordinates(name: str, states_data) -> tuple:
    """Get State Coordinates"""
    state_info = states_data[states_data.state == name]
    x = int(state_info.x.iloc[0])
    y = int(state_info.y.iloc[0])
    return x, y


def missing_states(guessed_states: list, all_states: list) -> list:
    """Create missing states list"""
    missing_states = [state for state in all_states if not state in guessed_states]
    return missing_states


# 4. Use a loop to allow the user to keep guessing
while len(total_answers) < len(state_list):
    # 1. Convert the guess to Title case
    answer_state = screen.textinput(
        title=f"{len(total_answers)}/50 States Correct",
        prompt="What's another state's name?",
    ).title()
    # 6. Kepp track of the score *line above*

    if answer_state == "Exit":
        states_to_learn = pd.DataFrame(
            missing_states(total_answers, state_list), columns=["state"]
        )
        states_to_learn.to_csv(r"Day_25\Game\states_to_learn.csv")
        break
    # 2. Check if the guess is among the 50 states
    if answer_state in state_list:
        if not answer_state in total_answers:
            answer_turtle.goto(states_cordinates(answer_state, df))
            # 3.2 Turtle write answer
            answer_turtle.write(answer_state)
            # 5. Record the correct guesses in a list
            total_answers.append(answer_state)


screen.exitonclick()
