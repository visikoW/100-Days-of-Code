from turtle import *

tim = Turtle()
screen = Screen()

def move_foward():
    tim.forward(10)

def move_backward():
    tim.back(10)

def move_counter_clockwise():
    new_heading = tim.setheading() + 10
    tim.setheading(new_heading)

def move_clockwise():
    new_heading = tim.setheading() - 10
    tim.setheading(new_heading)

def clear():
    tim.reset()

screen.listen()
screen.onkeypress(key = 'w', fun = move_foward)
screen.onkeypress(key = 's', fun = move_backward)
screen.onkeypress(key = 'a', fun = move_counter_clockwise)
screen.onkeypress(key = 'd', fun = move_clockwise)
screen.onkeypress(key = 'c', fun = clear)
screen.exitonclick()
