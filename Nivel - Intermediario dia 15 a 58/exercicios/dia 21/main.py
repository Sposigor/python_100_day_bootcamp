''' Exercicio do dia 21 - jogo de pong'''

from time import sleep
from turtle import Screen
from palito import Palito
from bola import Bola
from pontuação import Placar


palito_direita = Palito((350, 0))
palito_esquerda = Palito((-350, 0))
bola = Bola()
placar = Placar()

tela = Screen()
tela.tracer(0)
tela.setup(width=800, height=600)
tela.bgcolor('black')
tela.title('Ping Pong')

tela.listen()
tela.onkey(palito_direita.mover_cima, "Up")
tela.onkey(palito_direita.mover_baixo, "Down")
tela.onkey(palito_esquerda.mover_cima, "w")
tela.onkey(palito_esquerda.mover_baixo, "s")


jogo_ligado = True

while jogo_ligado:
    sleep(bola.movimento_bola)
    tela.update()
    bola.mover()

    # Colisão com a parede
    if bola.ycor() > 280 or bola.ycor() < -280:
        bola.salto_y()

    # Colisão com o palito
    if bola.distance(palito_direita) < 50 and bola.xcor() > 320 or bola.distance(palito_esquerda) < 50 and bola.xcor() < -320:
        bola.salto_x()

    # Ponto Direita
    if bola.xcor() > 380:
        placar.marca_ponto_direito()
        bola.reiniciar()
        bola.salto_x()
        sleep(0.3)

    # Ponto Esquerda
    if bola.xcor() < -380:
        placar.marca_ponto_esquerdo()
        bola.reiniciar()
        bola.salto_x()
        sleep(0.3)


tela.exitonclick()
