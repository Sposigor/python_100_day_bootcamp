''' Exercicio do dia 22 '''

from turtle import Turtle

posição_inicial = (0, -280)
distancia_movimento = 10
linha_chegada = 280


class Jogador(Turtle):
    ''' Jogador '''
    def __init__(self):
        ''' Inicialização '''
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.ir_para_o_próximo_nível()
        self.speed(0)
        self.setheading(90)

    def andar(self):
        ''' Movimentação para frente '''
        if self.ycor() < linha_chegada:
            self.sety(self.ycor() + distancia_movimento)

    def linha_de_chegada(self):
        ''' Verifica se chegou na linha de chegada '''
        if self.ycor() >= linha_chegada:
            return True
        return False

    def ir_para_o_próximo_nível(self):
        ''' Passa de nivel no jogo '''
        self.goto(posição_inicial)
