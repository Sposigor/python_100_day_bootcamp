''' Pontuação do jogo '''

from turtle import Turtle

alinhamento = 'center'
fonte = ('Arial', 20, 'normal')

class Pontuação(Turtle):
    ''' Registrar a pontuação do jogo '''

    def __init__(self):
        ''' Inicializa a classe mãe e registra a pontuação '''
        super().__init__()
        self.pontuação = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.atualizar_pontuacao()

    def atualizar_pontuacao(self):
        ''' Atualizar a informação na pontuação '''
        self.write(f'Pontuação: {self.pontuação}', font=fonte, align=alinhamento)

    def gameover(self):
        ''' Messagem de game over quando o jogo acaba ou você bate no rabo/parede '''
        self.goto(x=0, y=0)
        self.write('Game Over', font=fonte, align=alinhamento)

    def adicionar_ponto(self):
        ''' Adiciona pontos ao registro de pontuação '''
        self.pontuação += 1
        self.clear()
        self.atualizar_pontuacao()
