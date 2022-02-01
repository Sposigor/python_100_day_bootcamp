''' Projeto de leilao '''
from os import system, name

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)


lances = {}
reiniciar = False

def maior_lance(registro_lance):
    ''' Retorna o maior lance '''
    maior_lance_dado = 0
    vencedor = ""
    for lance in registro_lance:
        armazenar_lance = registro_lance[lance]
        if armazenar_lance > maior_lance_dado:
            maior_lance_dado = armazenar_lance
            vencedor = lance
    print(f"O vencedor é {vencedor} com o valor de R${maior_lance_dado}")

def clear():
    ''' Limpa o console '''
    if name == 'nt':
        _ = system('cls')

while not reiniciar:
    nome = input("Qual é seu nome?: ")
    valor_oferecido = int(input("Qaul é seu lance?: R$ "))
    lances[nome] = valor_oferecido
    continuar = input("Quer continuar com os lances? Digite 'sim' ou 'não'.\n")
    if continuar == "não":
        reiniciar = True
        maior_lance(lances)
    elif continuar == "sim":
        clear()
