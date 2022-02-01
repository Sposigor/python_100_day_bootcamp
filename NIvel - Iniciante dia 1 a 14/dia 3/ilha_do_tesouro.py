# Ilha do tesouro - Desafio da aula de hoje

''' Jogo interativo do ilha do tesouro. '''

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|________
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem vindo a ilha do tesouro.")
print("Sua missão é encontrar o tesouro.")

escolha1 = str(input("Você está perdido, existem dois caminhos, esquerda ou direita " +
                    "qual caminho ir? [direita/esquerda] ")).lower()


if escolha1 == "direita" or escolha1 == "d":
    escolha2 = input("Você chegou a um lago. Existe uma ilha no meio do lago. Digite 'esperar'"
        + " para esperar por um barco. Digite 'nadar' para atravessar a nado. ").lower()
    if escolha2 == "esperar" or escolha2 == "e":
        escolha3 = input("Você chega à ilha ileso. Existe uma casa com 3 portas. " +
            "Um 'vermelho', um 'amarelo' e um 'azul'. Qual cor você escolhe? "
            + "\n").lower()
        if escolha3 == 'vermelho':
            print("É uma sala cheia de fogo. Fim de jogo.")
        elif escolha3 == 'amarelo':
            print('Você encontrou o tesouro! Você ganhou!')
        elif escolha3 == 'azul':
            print('Você entra em uma sala de feras. Fim de jogo.')
        else:
            print('Você escolheu uma porta que não existe. Fim de jogo.')
    else:
        print('Você é atacado por um tubarão furioso. Fim de jogo.')
else:
    print("Você caiu em um buraco. Fim de jogo.")
