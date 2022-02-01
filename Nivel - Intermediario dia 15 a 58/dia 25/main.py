''' Exercicio do dia 25 '''

# bibliotecas utilizadas
import os
import turtle
#from achando_coor_do_mapa import AchaCoordenadas
import pandas as pd

# Variavel da imagem
imagem = os.path.abspath(r'Nivel - Intermediario dia 15 a 58\exercicios\dia 25\brasil.gif')

# Cenario com a função screen do turtle
cenario = turtle.Screen()
cenario.title('Jogo: Estados do Brasil')
cenario.addshape(imagem)


# Shape com a imagem usando o turtle
turtle.shape(imagem)

# Procurando as coordenadas do mapa
# turtle.onscreenclick(AchaCoordenadas().acha_coordenadas_com_mouse)

# Lendo o csv e criando uma lista com os estados
dados = pd.read_csv(r'Nivel - Intermediario dia 15 a 58\exercicios\dia 25\estados.csv')
todos_estados = dados.estado.tolist()

# while para pergunta, verificar e escrever o estado no mapa
estados_que_existem = []

while len(estados_que_existem) < 26:
    # Input do usuario para o nome do estado
    pergunta_estado = cenario.textinput(f"Estados {len(estados_que_existem)}|26",
                                        "Digite o nome do estado:")

    if pergunta_estado == 'Sair':
        break
    if pergunta_estado in todos_estados:
        estados_que_existem.append(pergunta_estado)
        aparece_nome_no_mapa = turtle.Turtle()
        aparece_nome_no_mapa.penup()
        aparece_nome_no_mapa.hideturtle()
        dados_estado = dados[dados.estado == pergunta_estado]
        aparece_nome_no_mapa.goto(int(dados_estado.x), int(dados_estado.y))
        aparece_nome_no_mapa.write(dados_estado.estado.item())

# gerar csv que contenha os estados que o usuario não acertou
dados_estados_que_nao_acertou = dados[~dados.estado.isin(estados_que_existem)]
dados_estados_que_nao_acertou.to_csv(r'Nivel - Intermediario dia 15 a 58\exercicios\dia 25\estados_que_nao_acertou.csv')
