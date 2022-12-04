from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.time_speed = 0.007
        self.speed(1)
        self.random_start()

    def random_start(self):
        self.setheading(randint(1, 359))

    def move(self):
        self.forward(1)

    def bounce_y(self):
        heading = self.heading()
        self.setheading(360 - heading)
        
    def bounce_x(self):
        heading = self.heading()
        self.setheading(180 - heading)
        if self.time_speed > 0.001:
            self.time_speed -= 0.001

    def reset(self):
        self.setpos(0, 0)
        self.random_start()
        self.time_speed = 0.007
