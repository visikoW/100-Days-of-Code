from turtle import Turtle

ALING = "center"
FONT = ("Courier", 30, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-180, 240)
        self.score = 0
        self.update()
        
    def update(self):
        self.clear()
        self.write(f"Level: {self.score}", False, ALING, FONT)
        
    def add(self):
        self.score += 1