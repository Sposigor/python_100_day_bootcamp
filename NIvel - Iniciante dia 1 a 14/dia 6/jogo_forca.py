''' Jogo da forca '''


import random
from jogo_forca_img import *
from jogo_forca_palavras import *
from replit import clear

print(logo)
jogo_finalizou = False
Vidas = len(estagios) - 1

escolha_palavra = random.choice(lista_palavras)
tamanho_palavra = len(escolha_palavra)

tela = []
for _ in range(tamanho_palavra):
    tela += ['_']

while not jogo_finalizou:
    encontrou = input('Digite uma letra: ').lower()
    clear()

    if encontrou in tela:
        print(f'Você já digitou essa {encontrou}')
    
    for posição in range(tamanho_palavra):
        carta = escolha_palavra[posição]
        if carta == encontrou:
            tela[posição] = carta
    print(f'{" ".join(tela)}')
    
    if encontrou not in escolha_palavra:
        Vidas -= 1
        print(f'Você errou, você tem {Vidas} vidas')
        print(estagios[Vidas])
        if Vidas == 0:
            print('Você perdeu')
            jogo_finalizou = True

    if not '_' in tela:
        print('Você venceu')
        jogo_finalizou = True