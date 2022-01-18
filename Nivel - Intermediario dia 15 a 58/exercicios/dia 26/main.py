''' Exercicio do dia 26 '''

import pandas as pd

nato = pd.read_csv(r'Nivel - Intermediario dia 15 a 58\exercicios\dia 26\nato_phonetic_alphabet.csv')

compreensão = {row.letra:row.codigo for (index, row) in nato.iterrows()}

palavra = input('Digite uma palavra: ').upper()
lista_palavra = [compreensão[letra] for letra in palavra]

print(lista_palavra)
