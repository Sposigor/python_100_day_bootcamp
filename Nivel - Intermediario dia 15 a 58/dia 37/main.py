''' Exercicio do dia 37 '''

from datetime import datetime
import requests


agora = datetime.now()
hoje = agora.strftime('%Y%m%d')
usuario = 'sposigor'
token = 'asdpoiqwepoijhd'
id_grafico = 'grafico1'
pixala_endpoint = 'https://pixe.la/v1/users'
grafico_endpoint = f'{pixala_endpoint}/{usuario}/graphs'
pixel_endpoint = f'{pixala_endpoint}/{usuario}/graphs/{id_grafico}'
atualizar_pixel = f'{pixala_endpoint}/{usuario}/graphs/{id_grafico}/{hoje}'
deletando_pixel = f'{pixala_endpoint}/{usuario}/graphs/{id_grafico}/{hoje}'

parametros_usuario = {
    'username': usuario,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
    'token': token
}

# criando_usuario = requests.post(url=pixala_endpoint_para_criar_usuario, json=parametros_usuario)
# print(criando_usuario.text)

graph_config_parametros = {
    'id': 'grafico1',
    'name': 'Tempo que fico usando o VS Code',
    'unit': 'minutes',
    'type': 'int',
    'color': 'sora',
}

header = {
    'X-USER-TOKEN': token
}

# fazendo_o_graph = requests.post(url=grafico_endpoint, json=graph_config_parametros, headers=header)
# print(fazendo_o_graph.text)


enviando_pixel_parametros = {
    'date': hoje,
    'quantity': input('Quantos minutos você usou o VS Code hoje?: ')
}

enviando_pixel = requests.post(url=pixel_endpoint, json=enviando_pixel_parametros, headers=header)
print(enviando_pixel.text)

atualizando_pixel_parametros = {
    'quantity': '450'
}

# atualizando_o_pixel = requests.put(url=atualizar_pixel, json=atualizando_pixel_parametros, headers=header)
# print(atualizando_o_pixel.text)

# deletando_pixel = requests.delete(url=deletando_pixel, headers=header)
# print(deletando_pixel.text)
