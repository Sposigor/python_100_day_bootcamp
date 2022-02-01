"""
Exercicio do dia 45, vamos começar a usar o BS para raspagem de dados na internet

! Conteudo relevante para os proximos dias

? Documentação do BS https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/

"""

from bs4 import BeautifulSoup

# bs4 é basicamente usado para raspar dados em HTML e XML, websites estaticos.

with open('Nivel - Intermediario dia 15 a 58/exercicios/dia 45/website.html', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

sopa = BeautifulSoup(conteudo, 'html.parser')

todos_tag_com_texto = sopa.find_all(name='a')

for tag in todos_tag_com_texto:
    print(tag.get('href'))

head = sopa.find(id='name')

print(head.text)

sessão = sopa.find(class_='heading')
print(sessão.text)
