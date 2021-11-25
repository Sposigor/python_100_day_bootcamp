''' Jogo de mais alto ou mais baixo '''
from os import system, name
import random
from base_dados import dados
from arte import logo, vs

def clear():
    ''' limpa a tela '''
    if name == 'nt':
        _ = system('cls')

def get_dados():
    ''' Retorna um informação aleatoria a partir da base.py'''
    return random.choice(dados)

def formatar_dados(conta):
    """Formata os dados da base.py"""
    nome = conta["nome"]
    descrição = conta["descrição"]
    pais = conta["pais"]
    return f"{nome}, que é {descrição}, do {pais}"

def pergunta(escolha, a_seguidor, b_seguidor):
    """Retorna a respota da pergunta"""
    if a_seguidor > b_seguidor:
        return escolha == "a"
    else:
        return escolha == "b"


def game():
    ''' Roda o jogo '''
    print(logo)
    pontuação = 0
    continua = True
    conta_a = get_dados()
    conta_b = get_dados()

    while continua:
        conta_a = conta_b
        conta_b = get_dados()

        while conta_a == conta_b:
            conta_b = get_dados()
    
        print(f"Compare A: {formatar_dados(conta_a)}.")
        print(vs)
        print(f"Contra B: {formatar_dados(conta_b)}.")
    
        escolha = input("Quem tem mais seguidores? Digito 'A' ou 'B': ").lower()
        a_quantidade_seguidores = conta_a["seguidores"]
        b_quantidade_seguidores = conta_b["seguidores"]
        qual_tem_mais = pergunta(escolha, a_quantidade_seguidores, b_quantidade_seguidores)
    
        clear()
        print(logo)
        if qual_tem_mais:
            pontuação += 1
            print(f"Você tem razão! Pontuação atual: {pontuação}.")
        else:
            continua = False
            print(f"Desculpe, isso está errado. Pontuação final: {pontuação}")

game()
