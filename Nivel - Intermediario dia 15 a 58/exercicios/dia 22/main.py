''' Exercicio do dia 22 '''

import time
from turtle import Screen
from jogador import Jogador
from carro import Carros
from placar import Placar


# Cenario
cenario = Screen()
cenario.setup(width=600, height=600)
cenario.tracer(0)

# Placar
placar = Placar()

# Jogador
jogador = Jogador()

# Carros
carros = Carros()

# Movimentação
cenario.listen()
cenario.onkey(jogador.andar, key="Up")

# Funcionamento do jogo
jogo_on = True
while jogo_on:
    time.sleep(0.1)
    cenario.update()

    # Criar carros
    carros.adicionar_carro()
    # Movimentar carros
    carros.mover_carros()

    # Verificar colisão
    for carro in carros.carros:
        if carro.distance(jogador) < 20:
            jogo_on = False
            placar.fim_de_jogo()


    # Verificar linha de chegada
    if jogador.linha_de_chegada():
        jogador.ir_para_o_próximo_nível()
        carros.acelerar_carros()
        placar.atualizar_pontuação()

cenario.exitonclick()
