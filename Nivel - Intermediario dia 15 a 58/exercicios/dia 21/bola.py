''' bola do ping pong '''

from turtle import Turtle

class Bola(Turtle):
    ''' Classe da bola do ping pong '''

    def __init__(self,):
        ''' Inicialização da classe '''
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.novo_x = 10
        self.novo_y = 10
        self.movimento_bola = 0.1

    def mover(self):
        ''' Mover a bolinha pelo campo conforme o jogo '''
        self.goto(self.xcor() + self.novo_x, self.ycor() + self.novo_y)

    def salto_y(self):
        ''' Salto da borda da tela na bolinha '''
        self.novo_y *= -1

    def salto_x(self):
        ''' Salto do palito na bolinha '''
        self.novo_x *= -1
        self.movimento_bola *= 0.9

    def reiniciar(self):
        ''' reinicia após marca um ponto '''
        self.goto(0, 0)
