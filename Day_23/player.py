from turtle import Turtle

START = (0, -280)

class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(START)
        
    def move(self):
        self.forward(8)
        
    def up(self):
        self.move()
        
    def restart(self):
        self.goto(START)
        