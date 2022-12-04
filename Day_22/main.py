import time
from turtle import Screen
from peddles import Peddles
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Ping-Pong")
screen.tracer(0)

r_paddle_color = screen.textinput("Digite a cor da sua barra", "aqui!")
r_paddle = Peddles((350, 0), r_paddle_color)
l_paddle_color = screen.textinput("Digite a cor da sua barra", "aqui!")
l_paddle = Peddles((-350, 0), l_paddle_color)
scoreboard = Scoreboard()
ball = Ball()

# Listen action on game
screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "i")
screen.onkeypress(r_paddle.down, "k")

is_game_on = True
while is_game_on:
    time.sleep(ball.time_speed)
    screen.update()
    ball.move()

    # Check collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Check collison with r_paddles
    if ball.xcor() + 20 >= r_paddle.xcor() and ball.distance(r_paddle) < 50:
        ball.bounce_x()

    # Check collison with l_paddles
    elif ball.xcor() <= l_paddle.xcor() + 20 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # Check ball out of bounds at rigth side
    if ball.xcor() >= 390:
        scoreboard.add_r()
        ball.reset()

    # Check ball out of bounds at rigth side
    elif ball.xcor() <= -390:
        scoreboard.add_l()
        ball.reset()

screen.exitonclick()
