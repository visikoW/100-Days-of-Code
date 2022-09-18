from turtle import *
from random import *

class MyTurtle:
    def __init__(self, turtle = Turtle()):
        self.turtle = turtle
        self.turtle.shape('turtle')
        self.screen = Screen()
        colormode(255)

    def new_line(self, distance):
        self.turtle.forward(distance)

    def turtle_speed(self, new_speed = 6):
        self.turtle.speed(new_speed)

    def pen_size(self, size):
        self.turtle.pensize(size)

    def jump(self, distance):
        self.turtle.penup()
        self.turtle.forward(distance)
        self.turtle.pendown()

    def random_color(self):
        R = randint(0, 255)
        G = randint(0, 255)
        B = randint(0, 255)
        return (R, G, B)
    
    def new_heading(self, number):
        current_heading = self.turtle.heading()
        self.turtle.setheading(current_heading + number)

    def create_format(self, edge):
        angular = 360/edge
        self.random_color()
        for x in range(0, edge):
            self.new_line(50)
            self.turtle.right(angular)

    def create_circle(self, radius):
        self.random_color()
        self.turtle.circle(radius)

    def random_walk(self, ways, length = 50):
        ways_lists = [0, 90, 180, 270]
        for x in range(0, ways + 1):
            self.random_color()
            self.new_line(length)
            self.turtle.setheading(choice(ways_lists))

    def dot_turtle(self, size):
        self.turtle.dot(size, self.random_color())

    def create_dot_square(self, x, y, size = 10, range_between = (20, 20)):
        self.turtle.shape('arrow')
        for i in range(0, y):
            for u in range(0, x):
                self.turtle.penup()
                self.turtle.setpos((u - 5) * range_between[0], (i - 5) * range_between[1])
                self.turtle.pendown()
                self.dot_turtle(size)
