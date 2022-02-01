''' Exercicio dia 35 '''

import requests
from twilio.rest import Client

minha_latitude = -23.660573
minha_longitude = -46.747007
chave_api = '70774a31cf0e4cb435d3ba6a4399b49e'
owm_endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
conta_sid = "AC895a73e7c37076a710082239d691a073"
token = "5fd57bc147b329f68b1463ce588a37e0"


# API do tempo
parametros = {
    'lat': minha_latitude,
    'lon': minha_longitude,
    'appid': chave_api
}

resposta = requests.get(owm_endpoint, parametros)
resposta.raise_for_status()
clima_dados = resposta.json()
clima = clima_dados['hourly'][:12]

vai_chove = False

for hora in clima:
    condição = hora['weather'][0]['id']
    if int(condição) < 700:
        vai_chove = True

if vai_chove:
    # Serviço de envio de SMS de alguma empresa obscura (Twilio)
    client = Client(conta_sid, token)

    message = client.messages \
                    .create(
                            body="Tá chovendo ai perto corre!!",
                            from_='+16072988448',
                            to='+5511985945738'
                    )

    print(message.sid)
else:
    print('Não vai chover')
