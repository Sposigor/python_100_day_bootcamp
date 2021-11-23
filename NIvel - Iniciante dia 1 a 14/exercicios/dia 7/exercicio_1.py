''' Adivinhação '''
import random


lista_palavra = ["jogo", "bola", "sapato"]

selecao_palavra = random.choice(lista_palavra)

print(selecao_palavra)

letra_usuario = input("Letra a procurar: ").lower()

for i in lista_palavra:
    for j in i:
        if j == letra_usuario:
            print("Certo")
        else:
            print("Errado")
