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
        with open("/home/vinycius/Programacao/Python/100-Days-of-Code/Day_24/data.txt", mode="r") as file:
            self.highest = int(file.read())
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
            with open("/home/vinycius/Programacao/Python/100-Days-of-Code/Day_24/data.txt", mode="w") as file:
                file.write(f"{self.highest}")
        self.score = 0
        self.update_scoreboard()
        