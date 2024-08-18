import turtle
import pandas as pd
import ctypes

screen = turtle.Screen()
screen.title("U.S. States Game")
WIDTH, HEIGHT = 800, 550
screen.setup(WIDTH + 4, HEIGHT + 8)

image = r"Day_25\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

states_data = pd.read_csv(r"Day_25\50_states.csv")
state_names = states_data["state"].to_list()
guessed_states = []


def check_answer_in_df(answer, list) -> bool:
    if answer.title() in list:
        list.remove(answer.title())
        return True
    else:
        return False


def get_cords_answer(answer, df):
    state_data = df[df["state"] == answer.title()]
    name = answer.title()
    x = state_data["x"].item()
    y = state_data["y"].item()
    return [name, (x, y)]


def create_name_on_screen(turtle, name, cordinates):
    turtle.goto(cordinates[0], cordinates[1])
    turtle.write(name)


while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?",
    )
    try:
        if answer_state == "Exit":
            missing_states = pd.DataFrame(state_names)
            missing_states.to_csv(r"Day_25\states_to_learn.csv")
        if check_answer_in_df(answer_state, state_names):
            state_info = get_cords_answer(answer_state, states_data)
            create_name_on_screen(pen, state_info[0], state_info[1])
            guessed_states.append(state_info[0])
    except AttributeError:
        ctypes.windll.user32.MessageBoxW(0, "Wrtie 'Exit' if done", "Cancel Button", 1)

ctypes.windll.user32.MessageBoxW(
    0, "Congratulations Click on Screen to exit", "You WIN!!!!", 1
)
screen.exitonclick()
