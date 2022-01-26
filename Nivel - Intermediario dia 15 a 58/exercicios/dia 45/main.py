"""
Exercicio do dia 45
"""

import requests
from bs4 import BeautifulSoup

resposta = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
website = resposta.text

sopa = BeautifulSoup(website, 'html.parser')

lista_filmes = sopa.find_all(name='h3', class_="title")

filmes_nomes = [i.getText() for i in lista_filmes]
filmes = filmes_nomes[::-1]


with open('Nivel - Intermediario dia 15 a 58/exercicios/dia 45/filmes.txt', 'w', encoding='utf-8') as arquivo:
    for i in filmes:
        arquivo.write(f'{i}\n')
