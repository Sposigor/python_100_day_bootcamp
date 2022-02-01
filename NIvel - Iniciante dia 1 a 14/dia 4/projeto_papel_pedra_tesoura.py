''' jogo de papel, pedra e tesoura '''

import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

imagem_jogo = [pedra, papel, tesoura]

escolha_user = int(input("Qual é sua escolha? Tipo 0 para pedra, 1 para papel ou 2 para tesoura.\n"))
print(imagem_jogo[escolha_user])

escolha_computador = random.randint(0, 2)
print("Escolha de Computador:")
print(imagem_jogo[escolha_computador])

if escolha_user >= 3 or escolha_user < 0:
    print("você digitou um numero errado, você perdeu!")
elif escolha_user == 0 and escolha_computador == 2:
    print("você venceu!")
elif escolha_computador == 0 and escolha_user == 2:
    print("você perdeu")
elif escolha_computador > escolha_user:
    print("você perdeu")
elif escolha_user > escolha_computador:
    print("você venceu!")
elif escolha_computador == escolha_user:
    print("Empate")
