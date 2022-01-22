''' Exercicio dia 34 '''

import requests

parametros = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parametros)
response.raise_for_status()
dados = response.json()
questão = dados["results"]
