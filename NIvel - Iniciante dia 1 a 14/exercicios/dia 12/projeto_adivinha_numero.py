''' Jogo de adivinhação do numero '''
import random
from os import system, name

logo = '''.
   ____              _     __                                               ___  
  / __ \            | |   /_/                                              |__ \ 
 | |  | |_   _  __ _| |   ___    ___    _ __  _   _ _ __ ___   ___ _ __ ___   ) |
 | |  | | | | |/ _` | |  / _ \  / _ \  | '_ \| | | | '_ ` _ \ / _ \ '__/ _ \ / / 
 | |__| | |_| | (_| | | |  __/ | (_) | | | | | |_| | | | | | |  __/ | | (_) |_|  
  \___\_\\__,_|\__,_|_ |  \___|  \___/  |_| |_|\__,_|_| |_| |_|\___|_|  \___/(_)  
'''

def menu():
    ''' Função que mostra o menu '''
    print(logo)
    print('\033[1;33mJogo de adivinhação do numero\033[m')
    print('\033[1;3m-=-\033[m' * 20)
    print('\033[1;33mEstou pensando em um numero entre 1 e 100\033[m')
    print('\033[1;33mVocê terá 5 chances para acertar o numero\033[m')
    print('\033[1;31m-=-\033[m' * 20)

def logica_jogo():
    ''' Função que faz a logica do jogo '''
    dificuldade = input("\033[1;317mSelecione a dificuldade: "
                        +"digite d para 'dificil' e f para 'facil': \033[m")
    if dificuldade == 'd':
        numero_secreto = random.randint(1, 100)
        numero_de_tentativas = 5
    elif dificuldade == 'f':
        numero_secreto = random.randint(1, 100)
        numero_de_tentativas = 10

    for rodada in range(1, numero_de_tentativas + 1):
        print(f'\033[1;317mTentativa {rodada} de {numero_de_tentativas}\033[m')
        chute = int(input('Digite um numero entre 1 e 100: '))
        if chute < 1 or chute > 100:
            print('\033[1;31mVocê deve digitar um numero entre 1 e 100\033[m')
            continue
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        if acertou:
            print('\033[1;32mVocê acertou!\033[m')
            break
        else:
            if maior:
                print('\033[1;31mVocê errou! O seu chute foi maior que o numero secreto\033[m')
            elif menor:
                print('\033[1;31mVocê errou! O seu chute foi menor que o numero secreto\033[m')
    print('\033[1;317mFim do jogo!\033[m')

def clear():
    ''' limpa a tela '''
    if name == 'nt':
        _ = system('cls')

def main():
    ''' Função principal '''
    clear()
    menu()
    logica_jogo()

main()
