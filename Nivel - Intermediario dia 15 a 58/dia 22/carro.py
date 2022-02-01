''' Exercicio do dia 22 '''

from turtle import Turtle
import random


cores = ["red", "orange", "yellow", "green", "blue", "purple"]
distancia_movimento_inicial = 5
aceleração = 5


class Carros:
    ''' Carros '''
    def __init__(self):
        ''' Inicialização '''
        self.carros = []
        self.velocidade_carro = distancia_movimento_inicial

    def adicionar_carro(self):
        ''' Adiciona carro '''
        chance_aleatoria = random.randint(0, 3)
        if chance_aleatoria == 1:
            carro = Turtle()
            carro.shape("square")
            carro.color(random.choice(cores))
            carro.penup()
            carro.speed(0)
            carro.shapesize(1, 2)
            random_y = random.randint(-250, 250)
            carro.goto(300, random_y)
            self.carros.append(carro)

    def mover_carros(self):
        ''' movimenta os carros ao longo da tela '''
        for carro in self.carros:
            carro.backward(self.velocidade_carro)

    def acelerar_carros(self):
        ''' acelera os carros '''
        self.velocidade_carro += aceleração
