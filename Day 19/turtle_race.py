from turtle import *
from random import *

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
ALL_TURTLES = []

screen = Screen()
screen.setup(width=600, height=600)

def create_race(colors):
    for x in range(len(colors)):
        newturtle = Turtle(shape = 'turtle')
        X = (-screen.window_width() / 2) + 50
        Y = (screen.window_height() / 2) - 175 - (x * 50)
        newturtle.color(colors[x])
        newturtle.shape("turtle")
        newturtle.penup()
        newturtle.goto(X,Y)
        newturtle.pendown()
        ALL_TURTLES.append(newturtle)

def race():
    continue_race = True
    user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color')
    while continue_race:
        for turtle in ALL_TURTLES:
            if turtle.xcor() > 240:
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                continue_race = False
            rand_distance = randint(0, 10)
            turtle.forward(rand_distance)

create_race(COLORS)
race()

screen.exitonclick()