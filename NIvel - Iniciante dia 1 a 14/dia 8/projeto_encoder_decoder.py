''' Gerando um encriptador e um decriptador de mensagens '''
from time import sleep
from tqdm import tqdm

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print('''
              .-') _  _ .-') _           _  .-')     ('-.   .-') _      ('-.     
             ( OO ) )( (  OO) )         ( \( -O )  _(  OO) (  OO) )    ( OO ).-. 
  ,-.-') ,--./ ,--,'  \     .'_   ,-.-') ,------. (,------./     '._   / . --. / 
  |  |OO)|   \ |  |\  ,`'--..._)  |  |OO)|   /`. ' |  .---'|'--...__)  | \-.  \  
  |  |  \|    \|  | ) |  |  \  '  |  |  \|  /  | | |  |    '--.  .--'.-'-'  |  | 
  |  |(_/|  .     |/  |  |   ' |  |  |(_/|  |_.' |(|  '--.    |  |    \| |_.'  | 
 ,|  |_.'|  |\    |   |  |   / : ,|  |_.'|  .  '.' |  .--'    |  |     |  .-.  | 
(_|  |   |  | \   |   |  '--'  /(_|  |   |  |\  \  |  `---.   |  |     |  | |  | 
  `--'   `--'  `--'   `-------'   `--'   `--' '--' `------'   `--'     `--' `--' ''')



def ceaser_cypher():
    ''' Encriptar e Descripitar uma mensagem '''
    resposta_usuario = input('Você quer encriptar ou descriptar?, digite "encriptar"' +
                                ' para encriptar ou "descriptar" para descriptar\n').lower()
    reposta_esperada = ['descriptar', 'encriptar']
    while resposta_usuario not in reposta_esperada:
        resposta_usuario = input('Por favor, digitar corretamento a instrução, '+
                                    'digite "encriptar para encriptar'+
                                    ' ou "descriptar" para descriptar\n')
    while True:
        try:
            deslocar = int(input('Por favor inserir a chave numerica para encriptar/descriptar:\n'))
        except ValueError:
            print('Por favor, somente numeros para chave numerica:')
            continue
        else:
            break

    deslocar %= 26

    if resposta_usuario == 'descriptar':
        deslocar = deslocar *-1

    texto_usuario = input(f'Por favor, digite a messagem para {resposta_usuario}:\n')
    print('Perfeito\n')
    print(f'Você está usando a chave de deslocamento: {deslocar}\n')
    print(f'Estamos trabalhando para {resposta_usuario}...\n')
    for i in tqdm(range(10)):
        sleep(0.1)

    resultado_final = ''

    for letra in texto_usuario:
        if letra in alfabeto:
            posição = alfabeto.index(letra)
            posição_final = posição + deslocar
            resultado_final += alfabeto[posição_final]
        else:
            resultado_final += letra
    print(f'Sistema terminou de {resposta_usuario}⤵:\n{resultado_final}')

ceaser_cypher()


reiniciar = ['sim', 'não']
novamente = True
while novamente:
    cypher_novamente = input('\nVocê quer continuar usando o programa?'+
                            ' digite "sim" para continuar ou "não" para finalizar\n').lower()

    while cypher_novamente not in reiniciar:
        cypher_novamente = input('\nPor favor digite corretamente os comandos,'+
                                ' digite "sim" para continuar ou "não" para finalizar\n').lower()
    if cypher_novamente == 'sim':
        ceaser_cypher()
    else:
        print('Obrigado e volte sempre.\n')
        novamente = False
