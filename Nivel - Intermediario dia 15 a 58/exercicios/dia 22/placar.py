''' Exercicio do dia 22 '''

from turtle import Turtle


class Placar(Turtle):
    ''' Registra a pontuação do placar '''

    def __init__(self):
        super().__init__()
        self.nivel = 1
        self.hideturtle()
        self.penup()
        self.goto(-230, 260)
        self.atualizar_placar()

    def atualizar_placar(self):
        ''' Atualizar o placar '''
        self.clear()
        self.write(f"Nivel: {self.nivel}", align="center", font=("Courier", 16, "normal"))

    def atualizar_pontuação(self):
        ''' Atualizar a pontuação '''
        self.nivel += 1
        self.atualizar_placar()

    def fim_de_jogo(self):
        ''' Message de fim de jogo '''
        self.goto(0, 0)
        self.write("Fim de jogo", align="center", font=("Courier", 16, "normal"))
