from turtle import Screen, Turtle, shape
import pandas as pd

# Define the path to the dataset and the image
PATH = "/home/vinycius/Programacao/Python/100-Days-of-Code/Day_25/us_states_game/"
IMAGE_PATH = f"{PATH}blank_states_img.gif"
DATA_PATH = pd.read_csv(f"{PATH}50_states.csv")

# Create the turtle screen and set the title
screen = Screen()
screen.title("U.S States Game")

# Set the screen background image
screen.bgpic(IMAGE_PATH)

# Create a turtle to write the state names
t = Turtle()
t.speed(0)
t.hideturtle()

# Define the way how the turtle sould write the state names
def turtle_write(state: str, x: int, y: int):
    t.pu()
    t.goto(x, y)
    t.write(state, align="center", font=("Arial", 8, "normal"))

# Starts with 0 points
player_points = 0

# All who you write correctly
corrects_answers = pd.DataFrame(columns=["state", "x", "y"])

while player_points < 50:
    answer_state = screen.textinput(
        title="Guess the State" if player_points == 0 else f"{player_points}/50 Guess the State",
        prompt="What's another state's name?"
    )

    if answer_state == None:
        break

    answer_state = str(answer_state).title()
    state_data = DATA_PATH[DATA_PATH['state'] == answer_state]

    if not state_data.empty:
        player_points += 1
        
        current_answer = state_data.index[0]
        current_x, current_y = state_data.at[current_answer, 'x'], state_data.at[current_answer, 'y']

        DATA_PATH.drop(state_data.index[0], inplace = True)
        turtle_write(answer_state, current_x, current_y)

        corrects_answers.add(state_data)
        print(type(corrects_answers))

turtle_write("You have reached the maximum point!", 0, -200)
