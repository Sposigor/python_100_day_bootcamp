''' Função para encontrar as coordenadas no mapa usando o turtle '''

from turtle import Turtle

class AchaCoordenadas(Turtle):
    ''' Classe da procura das coordenadas '''

    def __init__(self):
        super().__init__()

    def acha_coordenadas_com_mouse(self, coordenada_x, coordenada_y):
        ''' Função para encontrar as coordenadas no mapa usando o mouse '''
        print(f'Coordenadas do mouse: {coordenada_x}, {coordenada_y}')
