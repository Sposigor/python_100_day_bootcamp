"""
Continuação do exercicio 45, usando bs4 para raspagem de dados em websites online

! Alerta de conteudo relevante para os estudos

"""
from bs4 import BeautifulSoup
import requests

resposta = requests.get("https://news.ycombinator.com/news")
texto_site = resposta.text

sopa = BeautifulSoup(texto_site, 'html.parser')

artigos_tag = sopa.find_all('a', class_='titlelink')
texto_artigos = []
links_artigos = []

for i in artigos_tag:
    texto = i.getText()
    link = i.get('href')
    texto_artigos.append(texto)
    links_artigos.append(link)

artigos_votados = [int(x.getText().split()[0]) for x in sopa.find_all(name='span', class_='score')]

print(texto_artigos)
print(links_artigos)
print(artigos_votados)

mais_votado = max(artigos_votados)
index_mais_votado = artigos_votados.index(mais_votado)
print(f'O artigo mais votado é o {texto_artigos[index_mais_votado]}, acessar em: {links_artigos[index_mais_votado]} com {max(artigos_votados)} votos')
