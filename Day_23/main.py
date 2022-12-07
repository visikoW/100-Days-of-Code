import time
from score import Score
from turtle import Screen
from player import Player
from random import randint
from car_manager import CarManager

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class Game:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.bgcolor("white")
        self.screen.title("Turtle overtaking")
        self.screen.tracer(0)

        self.player = Player()
        self.score = Score()
        self.car_manager = CarManager()

    def play(self):
        is_game_on = True

        self.screen.listen()
        self.screen.onkeypress(self.player.up, 'w')

        while is_game_on:
            time.sleep(0.007)
            self.screen.update()
            self.score.update()

            self.car_manager.create_cars()
            self.car_manager.move_cars()
            
            # Check player collision with car_manager
            if self.car_manager.is_collision_with_player(self.player):
                is_game_on = False
            
            # Check if the player is already reached the end_of_game
            if self.player.ycor() >= 280:
                self.player.restart()
                self.score.add()
                self.car_manager.restart()
                self.car_manager.more_speed()

        self.screen.exitonclick()


game = Game()

game.play()
