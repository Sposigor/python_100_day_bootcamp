''' Calculadora simples com funções '''
from os import system, name


logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | primeiro_n | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(primeiro_n, segundo_n):
    ''' Soma dois números '''
    return primeiro_n + segundo_n
def sub(primeiro_n, segundo_n):
    ''' Subtração dois números '''
    return primeiro_n - segundo_n
def multiplicar(primeiro_n, segundo_n):
    ''' Multiplicar dois números '''
    return primeiro_n * segundo_n
def dividir(primeiro_n, segundo_n):
    ''' Dividir dois números '''
    return primeiro_n / segundo_n


operações = {
    "+": add,
    "-": sub,
    "*": multiplicar,
    "/": dividir
}


def clear():
    ''' Limpa o console '''
    if name == 'nt':
        _ = system('cls')

def menu():
    ''' Calculadora '''
    print(logo)
    print("\nBem vindo")
    primeiro_numero = int(input('Digite o primeiro número: '))
    for i in operações:
        print(i)
    continuar = True

    while continuar:
        operador = input("Digite o operador: ")
        segundo_numero = int(input("Digite o proximo numero: "))
        calcular = operações[operador]
        resultado = calcular(primeiro_numero, segundo_numero)
        print(f"{primeiro_numero} {operador} {segundo_numero} = {resultado}")

        if input(f"Digite 's' para continuar calculando com o resultado {resultado} ou" +
                    "digite 'n' para reiniciar a calculadora: ") == "s":
            primeiro_numero = resultado
        else:
            continuar = False
            clear()
            menu()
menu()
