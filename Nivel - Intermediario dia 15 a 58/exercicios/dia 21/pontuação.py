''' Placar do jogo de ping pong '''

from turtle import Turtle

class Placar(Turtle):
    ''' Placar do jogo de pinp pong '''

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.placar_direito = 0
        self.placar_esquerdo = 0
        self.placar_e_atualizar_o_placar()

    def placar_e_atualizar_o_placar(self):
        ''' Placar e também atualiza o placar '''
        self.clear()
        self.goto(-100, 200)
        self.write(self.placar_direito, align="center", font=("Arial", 65, "normal"))
        self.goto(100, 200)
        self.write(self.placar_esquerdo, align="center", font=("Arial", 65, "normal"))

    def marca_ponto_direito(self):
        ''' Atualiza a pontuação '''
        self.placar_direito += 1
        self.placar_e_atualizar_o_placar()

    def marca_ponto_esquerdo(self):
        ''' Atualiza a pontuação '''
        self.placar_esquerdo += 1
        self.placar_e_atualizar_o_placar()
