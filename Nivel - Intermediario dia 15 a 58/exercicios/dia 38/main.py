''' Exercicio dia 38 '''

from datetime import datetime
import requests



app_id = '974cc297'
api_key = '8d9bf74f139716b87012f9ea725b124f'

headers = {
    'x-app-id': app_id,
    'x-app-key': api_key,
}

genero = "masculino"
peso = '75'
altura = '179'
idade = '25'

exercicio_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
planilha_endpoint = 'https://api.sheety.co/57aaaadef6bb280e20414d3f2e03a33b/exercicioPythonDia38/test'

texto_exercicio = input("Qual exercicio você fez: ")


parametros = {
    "query": texto_exercicio,
    "gender": genero,
    "weight_kg": peso,
    "height_cm": altura,
    "age": idade
}

Bearer = {
    "Authorization": 'Bearer tokensecreto'
}

resposta = requests.post(exercicio_endpoint, json=parametros, headers=headers)
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

    resposta_planilha = requests.post(planilha_endpoint, json=input_planilha, headers=Bearer)
    print(resposta_planilha.text)
