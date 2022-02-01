''' Gerador de senha aleatória '''
import random

# Gerador de senha
print('=' * 30)
print('Gerador de senha')
print('=' * 30)

# Gerador de senha
def gerador_de_senhas():
    ''' Gerador de senha '''
    # Lista de caracteres
    caracteres = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numericos = list('0123456789')
    especiais = list('!@#$%&*')
    # Opções da senha
    total_de_caracteres = int(input('Quantos caracteres você deseja na sua senha? '))
    quantidade_numeros = int(input('Quantidade de numeros: '))
    quantidade_especiais = int(input('Quantidade de caracteres especiais: '))
    # Gerando a senha
    senha = []
    for i in range(total_de_caracteres):
        if i < quantidade_numeros:
            senha.append(random.choice(numericos))
        elif i < quantidade_numeros + quantidade_especiais:
            senha.append(random.choice(especiais))
        else:
            senha.append(random.choice(caracteres))
    return print(f"Sua senha é: {''.join(senha)}")

gerador_de_senhas()
