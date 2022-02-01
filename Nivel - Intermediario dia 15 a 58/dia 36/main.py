''' Exercicio dia 36 '''

import requests
from twilio.rest import Client


ação = "TSLA"
nome_empresa = "Tesla Inc"
tipo_função_ações = "TIME_SERIES_DAILY"
key_alpha_vantage = "H8CVBCDBWC690MHR"
key_novas_noticias = 'f04ae4e8c1a64fe9bffa933d32d468ff'
conta_sid = "AC895a73e7c37076a710082239d691a073"
token = "a8d1d187e5718d02c5e2f2de4598d838"


## PASSO 1: Use https://www.alphavantage.co
# Quando o preço das AÇÕES aumenta/diminui em 5% entre ontem e anteontem, imprima("Obter notícias").

# Parametros da API (https://www.alphavantage.co/documentation/)
parametros = {
    'function': tipo_função_ações,
    'symbol': ação,
    'apikey': key_alpha_vantage
}

# Fazendo a requisição
url = 'https://www.alphavantage.co/query'
resposta = requests.get(url, params=parametros)

# Transformando a resposta em JSON
raw = resposta.json()['Time Series (Daily)']

# Ajustando os dados para trazer a ultima data disponivel
raw_lista = [valores for (chave, valores) in raw.items()]
dados = raw_lista[0]
dados_fechamento_ontem = dados['4. close']

# Ajustando os dados para trazer a penultima data disponivel
dados2 = raw_lista[1]
dados_fechamento_anteontem = dados2['4. close']

# Diferença entre o fechamento de ontem e anteontem
diferença = float(dados_fechamento_ontem) - float(dados_fechamento_anteontem)
sobe_desce = None
if diferença > 0:
    sobe_desce = '⬆️'
else:
    sobe_desce = '⬇️'


# Se a diferença for maior que 5% imprima("Obter notícias")
diferença_percentual = round((diferença / float(dados_fechamento_anteontem)) * 100)
#if diferença_percentual > 5:
#   print("Obter notícias")


## PASSO 2: Use https://newsapi.org
# Em vez de imprimir ("Obter notícias"), na verdade, obtenha as 3 primeiras notícias para a COMPANY_NAME.

# Parametros da API (https://newsapi.org/docs/endpoints/everything)
if abs(diferença_percentual) > 4:
    parametros2 = {
        'qInTitle' : nome_empresa,
        'apiKey' : key_novas_noticias
    }

# Fazendo a requisição
url2 = 'https://newsapi.org/v2/everything'
resposta2 = requests.get(url2, params=parametros2)

# Buscando apenas os artigos dentro do JSON
artigos = resposta2.json()['articles']

# Imprimindo os 3 primeiros artigos
tres_artigos = artigos[:3]


## PASSO 3: Use https://www.twilio.com
# Envie uma mensagem separada com a alteração percentual e o
# título e a descrição de cada artigo para o seu número de telefone.

# Pegandos as noticias e ajustando para o formato do SMS
artigos_formatados_para_SMS = [f'{ação}: {sobe_desce}{diferença_percentual}%\nTitulo: {artigo["title"]} \nDescrição: {artigo["description"]}' for artigo in tres_artigos]

client = Client(conta_sid, token)

for artigos in artigos_formatados_para_SMS:

    messagem = client.messages \
                    .create(
                            body=artigos,
                            from_='+16072988448',
                            to='+5511985945738'
                    )
    
    messagem = client.messages \
                    .create(
                            body=artigos,
                            from_='+16072988448',
                            to='+5511954925751'
                    )
