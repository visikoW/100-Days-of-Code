from random import choice, randint
from turtle import Turtle

COLORS = ["blue", "green", "yellow", "black", "purple", "red", "orange"]
MOVE_SPEED = 1

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.move_distance = MOVE_SPEED

    def create_cars(self):
        random_chance = randint(1, 50)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.speed(1)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y = randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
        
    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.move_distance)

    def restart(self):
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars = []
        
    def verify_collision(self, player: Turtle) -> bool:
        for car in self.all_cars:
            if car.distance(player) <= 20:
                print(player.xcor())
                print(car.xcor())
                print(car.distance(player))
                return True
        return False
        
    def more_speed(self):
        self.move_distance += MOVE_SPEED
