from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        self.highest = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   higest: {self.highest}", False, ALIGNMENT, FONT)
        
    def add(self):
        self.score += 1
        self.update_scoreboard()
                
    def reset(self):
        if self.score > self.highest:
            self.highest = self.score
        self.score = 0
        self.update_scoreboard()
