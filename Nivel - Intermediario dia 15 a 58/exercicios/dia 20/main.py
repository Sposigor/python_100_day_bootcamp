''' Exercicio do dia 20 '''

from turtle import Screen
from time import sleep
from cobra import Cobra

cobra = Cobra()
jogo_esta_online = True

# Objeto da classe Screen
cenario = Screen()
cenario.setup(width=600, height=600)
cenario.bgcolor('black')
cenario.title('Ilha das Cobras')
cenario.tracer(0)
cenario.listen()
cenario.onkey(cobra.mover_para_direita, 'Right')
cenario.onkey(cobra.mover_para_esquerda, 'Left')
cenario.onkey(cobra.mover_para_cima, 'Up')
cenario.onkey(cobra.mover_para_baixo, 'Down')


while jogo_esta_online:
    cenario.update()
    sleep(0.1)
    cobra.mover_cobra()











cenario.exitonclick()
