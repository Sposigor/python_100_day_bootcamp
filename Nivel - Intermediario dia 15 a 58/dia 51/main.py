"""
Exercicio do dia 51

"""
from time import sleep
from teste_internet import TesteInternet


# Variaveis
NET_DOWN_PROMETIDA = 300
NET_UP_PROMETIDA = 150

robozinho = TesteInternet()
robozinho.pegar_velocidade_net()


sleep(10)

if NET_DOWN_PROMETIDA > robozinho.baixar or NET_UP_PROMETIDA < robozinho.subir:
    robozinho.envinado_messagem_twiter()
else:
    print(f'Velocidade da internet: {robozinho.subir} Mbps de upload e {robozinho.baixar} Mbps de download')
