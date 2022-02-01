# calculadora de gorjeta em uma conta

''' Calcula a gorjeta de uma conta e mostra o valor total '''

print('Calculadora de gorjeta')
total_conta = float(input('Digite o valor total da conta: '))
total_pessoas_consumo = int(input('Digite o número de pessoas que consumiram: '))
percentual_gorjeta = float(input('Digite o percentual de gorjeta: 10, 12 ou 20: '))
if percentual_gorjeta == 10:
    gorjeta = total_conta * 0.1
    print(f'O valor da gorjeta é de R$ {gorjeta:.2f}')
    print(f'O valor total da conta é de R$ {total_conta + gorjeta:.2f}')
    print(f'O valor de cada pessoa é {(total_conta + gorjeta)/total_pessoas_consumo:.2f}')
elif percentual_gorjeta == 12:
    gorjeta = total_conta * 0.12
    print(f'O valor da gorjeta é de R$ {gorjeta:.2f}')
    print(f'O valor total da conta é de R$ {total_conta + gorjeta:.2f}')
    print(f'O valor de cada pessoa é {(total_conta + gorjeta)/total_pessoas_consumo:.2f}')
elif percentual_gorjeta == 20:
    gojerjeta = total_conta * 0.2
    print(f'O valor da gorjeta é de R$ {gorjeta:.2f}')
    print(f'O valor total da conta é de R$ {total_conta + gorjeta:.2f}')
    print(f'O valor de cada pessoa é {(total_conta + gorjeta)/total_pessoas_consumo:.2f}')
