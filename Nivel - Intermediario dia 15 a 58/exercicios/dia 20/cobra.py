''' Usando a orientação a objetos, crie uma classe que represente uma cobra.'''

from turtle import Turtle

posição_inicial_x = [0, -20, -40]
andar_para_frente = 20
alto = 90
baixo = 270
esquerda = 180
direita = 0

class Cobra:
    ''' Classe da cobrinha do jogo '''

    def __init__(self):
        ''' Inicialização da classe '''
        self.cobra = []
        self.cobrinha()
        self.head = self.cobra[0]

    def cobrinha(self):
        ''' cobrinha do jogo '''
        cobrinha = Turtle()
        posição_inicial = posição_inicial_x
        for i in range(0, 3):
            cobrinha = Turtle('square')
            cobrinha.color("white")
            cobrinha.penup()
            cobrinha.goto(x=posição_inicial[i], y=0)
            self.cobra.append(cobrinha)

    def mover_cobra(self):
        ''' Movimenta a cobrinha automatico'''
        for i in range(len(self.cobra) - 1, 0, -1):
            self.cobra[i].goto(x=self.cobra[i-1].xcor(), y=self.cobra[i-1].ycor())
        self.head.forward(andar_para_frente)

    def mover_para_direita(self):
        ''' Muda a direção para direita sempre no angulo de 90 graus '''
        if self.head.heading() != esquerda:
            self.head.setheading(direita)

    def mover_para_esquerda(self):
        ''' Muda a direção para esquerda sempre no angulo de 90 graus '''
        if self.head.heading() != direita:
            self.head.setheading(esquerda)

    def mover_para_cima(self):
        ''' Muda a direção para cima sempre no angulo de 90 graus '''
        if self.head.heading() != baixo:
            self.head.setheading(alto)


    def mover_para_baixo(self):
        ''' Muda a direção para baixo sempre no angulo de 90 graus '''
        if self.head.heading() != alto:
            self.head.setheading(baixo)
