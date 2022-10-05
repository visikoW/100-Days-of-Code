from turtle import *

tim = Turtle()
screen = Screen()

def move_foward():
    tim.forward(10)

screen.listen()
screen.onkey(key = 'space', fun = move_foward)
screen.exitonclick()