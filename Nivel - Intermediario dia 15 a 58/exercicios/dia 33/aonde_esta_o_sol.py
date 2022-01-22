''' API sobre a localização e o tempo do sol '''

from datetime import datetime
import requests


minha_latitude = -23.533773
minha_longitude = -46.625290
formato_hora = 0


parametros_de_acesso_api = {
    'lat': minha_latitude,
    'lgn': minha_longitude,
    'formatted': formato_hora
}

resposta = requests.get('https://api.sunrise-sunset.org/json', params=parametros_de_acesso_api)
resposta.raise_for_status()
dados = resposta.json()
nascer_sol = int(dados['results']['sunrise'].split("T")[1].split(":")[0])
por_do_sol = int(dados['results']['sunset'].split("T")[1].split(":")[0])

agora = datetime.now()
print(f"Agora é {agora.hour}h e o sol nasceu as {nascer_sol}h e vai se por as {por_do_sol}h")
