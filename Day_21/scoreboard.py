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
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)
        
    def add(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
