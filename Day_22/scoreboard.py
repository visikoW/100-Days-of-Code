from turtle import Turtle

FONT = ("Courier", 60, "normal")
ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.points()
        
    def points(self):
        self.clear()
        self.goto((-100, 200))
        self.write(self.l_score, False, ALIGN, FONT)
        self.goto((100, 200))
        self.write(self.r_score, False, ALIGN, FONT)
        
    def add_r(self):
        self.r_score += 1
        self.points()
        
    def add_l(self):
        self.l_score += 1
        self.points()