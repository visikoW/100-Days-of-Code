from turtle import Turtle

MOVE_DISTANCE = 20

class Peddles(Turtle):
    def __init__(self, position, color='white'):
        super().__init__("square")
        self.color(color)
        self.turtlesize(5, 1)
        self.pu()
        self.goto(position)
    
    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        
    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)