from turtle import *
from random import randint
from time import sleep

# criando classe tartarugas

class Tartaruga(Turtle):
    def __init__(self, numero, cor, x, y):
        super().__init__()

        self.hideturtle()
        self.speed(0)
        self.penup()
        self.color(cor)
        self.goto(x, y)
        self.shape("turtle")
        self.shapesize(2)
        self.pendown()
        self.showturtle
        self.numero = numero # id da Tartaruga

    def correr(self, x, y):
        self.goto(x, y)

# escopo global
x = -220
y = 160
cores = ["red", "green", "blue", "yellow", "grey", "purple"]
tartarugas = []

# criando janela
janela = Screen()
janela.setup(500,400)
janela.title("Jogo das Tartarugas Animadas")
janela.bgcolor("#FFFFFF")

# criando linha de chegada
linha = Turtle()
linha.hideturtle()
linha.penup()
linha.speed(0)
linha.goto(235, 195)
linha.color("#FF0000")
linha.pensize(2)
linha.pendown()
linha.goto(235, -195)


for i in range(len(cores)):
    print(x,y)
    tartarugas.append(Tartaruga(i, cores[i], x, y))
    y -= 75






janela.mainloop()