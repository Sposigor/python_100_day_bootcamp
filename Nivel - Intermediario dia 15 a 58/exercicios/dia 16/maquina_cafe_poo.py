''' Maquina de cafe com POO '''

from maquina_dinheiro import MaquinaDinheiro
from faz_cafe import FazCafe
from menu import Menu

maquina_dinheiro = MaquinaDinheiro()
faz_cafe = FazCafe()
menu = Menu()

continuar = True

while continuar:
    opcoes = menu.get_item()
    escolha = input(f"O que você gostaria? ({opcoes}): ")
    if escolha == "desligar":
        continuar = False
    elif escolha == "relatorio":
        faz_cafe.relatorio()
        maquina_dinheiro.relatorio()
    else:
        bebida = menu.encontrar_bebida(escolha)

        if faz_cafe.ingredientes_suficientes(bebida) and maquina_dinheiro.pagamento(bebida.custo):
            faz_cafe.faz_cafe(bebida)
