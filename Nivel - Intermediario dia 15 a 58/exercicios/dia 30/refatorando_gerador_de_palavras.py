''' Exercicio do dia 30 '''

import pandas as pd

nato = pd.read_csv(r'Nivel - Intermediario dia 15 a 58\exercicios\dia 26\nato_phonetic_alphabet.csv')

compreensão = {row.letra:row.codigo for (index, row) in nato.iterrows()}

def gerador_palavras():
    ''' Gerador de palavras e correção de alguns bugs '''
    palavra = input('Digite uma palavra: ').upper()
    try:
        lista_palavra = [compreensão[letra] for letra in palavra]
    except KeyError:
        print('Digite somentes letras para forma a palavra, numeros e simbolos não possuem retorno')
        gerador_palavras()
    else:
        print(lista_palavra)

gerador_palavras()