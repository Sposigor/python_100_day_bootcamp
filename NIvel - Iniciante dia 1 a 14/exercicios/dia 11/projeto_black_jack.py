''' Jogo de black jack '''
import random
from os import system, name


logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def clear():
    ''' Limpa o console '''
    if name == 'nt':
        _ = system('cls')

def escolher_carta():
    """retorna cartas aleatorias do baralho"""
    baralho = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cartas = random.choice(baralho)
    return cartas

def calcular_pontuacao(baralho):
    """Retorna a pontuação"""
    if sum(baralho) == 21 and len(baralho) == 2:
        return 0
    if 11 in baralho and sum(baralho) > 21:
        baralho.remove(11)
        baralho.append(1)
    return sum(baralho)

def compara_resultado(usuario_pontuacao, computador_pontuacao):
    ''' Retorna o vencedor '''
    if usuario_pontuacao > 21 and computador_pontuacao > 21:
        return "Ambos perderam com estouro de pontuação 😤"


    if usuario_pontuacao == computador_pontuacao:
        return "Empate 🙃"
    elif computador_pontuacao == 0:
        return "Perdeu, computador deu Blackjack 😱"
    elif usuario_pontuacao == 0:
        return "Venceu com o Blackjack 😎"
    elif usuario_pontuacao > 21:
        return "Você perdeu, estouro de pontuação 😭"
    elif computador_pontuacao > 21:
        return "Computador perdeu por estouro de pontuação 😁"
    elif usuario_pontuacao > computador_pontuacao:
        return "Venceu 😃"
    else:
        return "Perdeu 😤"

def jogar():
    ''' Iniciar o jogo '''
    print(logo)

    usuario_baralho = []
    computador_baralho = []
    fim_de_jogo = False

    for _ in range(2):
        usuario_baralho.append(escolher_carta())
        computador_baralho.append(escolher_carta())

    while not fim_de_jogo:
        usuario_pontuacao = calcular_pontuacao(usuario_baralho)
        computador_pontuacao = calcular_pontuacao(computador_baralho)
        print(f"   Seu baralho: {usuario_baralho}, pontuação: {usuario_pontuacao}")
        print(f"   Cartas do computador: {computador_baralho[0]}")

        if usuario_pontuacao == 0 or computador_pontuacao == 0 or usuario_pontuacao > 21:
            fim_de_jogo = True
        else:
            continuar_jogando = input("Digite 's' para receber mais uma carta, "+
                                        "digite 'n' para passar: ")
            if continuar_jogando == "y":
                usuario_baralho.append(escolher_carta())
            else:
                fim_de_jogo = True

    while computador_pontuacao != 0 and computador_pontuacao < 17:
        computador_baralho.append(escolher_carta())
        computador_pontuacao = calcular_pontuacao(computador_baralho)

    print(f"   Sua mão final: {usuario_baralho}, pontuação final: {usuario_pontuacao}")
    print(f"   Mão final do computador: {computador_baralho},"+
            f"pontuação final: {computador_pontuacao}")
    print(compara_resultado(usuario_pontuacao, computador_pontuacao))

while input("Você quer jogar Blackjack? Digite 's' ou 'n': ") == "s":
    clear()
    jogar()
