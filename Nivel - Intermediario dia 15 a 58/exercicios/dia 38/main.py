''' Exercicio dia 38 '''

from datetime import datetime
import requests



APP_ID = '974cc297'
API_KEY = '8d9bf74f139716b87012f9ea725b124f'

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

GENERO = "masculino"
PESO = '75'
ALTURA = '179'
IDADE = '25'

EXERCICIO_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
PLANILHA_ENDPOINT = 'https://api.sheety.co/57aaaadef6bb280e20414d3f2e03a33b/exercicioPythonDia38/test'

texto_exercicio = input("Qual exercicio você fez: ")


parametros = {
    "query": texto_exercicio,
    "gender": GENERO,
    "weight_kg": PESO,
    "height_cm": ALTURA,
    "age": IDADE
}

Bearer = {
    "Authorization": 'Bearer tokensecreto'
}

resposta = requests.post(EXERCICIO_ENDPOINT, json=parametros, headers=headers)
resultado = resposta.json()
print(resultado)

hoje = datetime.now().strftime("%d/%m/%Y")
hora_atual = datetime.now().strftime("%X")

for exercicio in resultado["exercises"]:

    input_planilha = {
        "test": {
            "date": hoje,
            "time": hora_atual,
            "exercise": exercicio["name"].title(),
            "duration": exercicio["duration_min"],
            "calories": exercicio["nf_calories"]
        }
    }

    resposta_planilha = requests.post(PLANILHA_ENDPOINT, json=input_planilha, headers=Bearer)
    print(resposta_planilha.text)
