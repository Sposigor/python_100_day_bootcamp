''' Palito de pong '''

from turtle import Turtle

alto = 90
baixo = 270

class Palito(Turtle):
    ''' Classe para criar o palito '''

    def __init__(self, posição):
        ''' Inicialização da classe '''
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.resizemode('user')
        self.turtlesize(5,1)
        self.goto(posição)

    def mover_cima(self):
        ''' Move para cima '''
        novo_y = self.ycor() + 20
        self.goto(self.xcor(), novo_y)

    def mover_baixo(self):
        ''' Move para baixo '''
        novo_y = self.ycor() - 20
        self.goto(self.xcor(), novo_y)
