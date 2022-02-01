''' Exercicio da aula 18 e vamos desenhar um tartaruga com o turtle '''

from turtle import Turtle, Screen
import random

tartaruga = Turtle()

tartaruga.shape('turtle')
tartaruga.screen.bgcolor('black')
tartaruga.color('white')
tartaruga.pensize(2)


cenario = Screen()
cenario.colormode(255)

# Tartaruga fazendo um quadrado

#for i in range(4):
#    tartaruga.forward(100)
#    tartaruga.left(90)

# Tartaruga fazendo uma linha tracejada
#for i in range(25):
#    tartaruga.penup()
#    tartaruga.forward(10)
#    tartaruga.pendown()
#    tartaruga.forward(10)


# Tartaruga fazendo diversos angulos em cores aleatorias
#
#cores = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'cyan']
#
#def desenhar_angulos(numero_lados):
#    ''' Desenha angulos com o turtle '''
#    angulo = 360 / numero_lados
#    for i in range(numero_lados):
#        tartaruga.forward(75)
#        tartaruga.left(angulo)
#
#for lados in range(3, 12):
#    tartaruga.color(random.choice(cores))
#    desenhar_angulos(lados)
#


# Tartaruga fazendo o random walk com cores aleatorias
#direção = [0, 90, 180, 270]
#velocidade = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#for i in range(100):
#    r = int(random.randint(1, 255))
#    g = int(random.randint(1, 255))
#    b = int(random.randint(1, 255))
#    color = (r, g, b)
#    tartaruga.pencolor(color)
#    tartaruga.speed(random.choice(velocidade))
#    tartaruga.forward(25)
#    tartaruga.setheading(random.choice(direção))
#


# Tartaruga fazendo espiral de circulos em cores aleatorias
#def cor_aleatoria():
#    ''' Gera uma cor aleatoria '''
#    r_color = int(random.randint(1, 255))
#    g_color = int(random.randint(1, 255))
#    b_color = int(random.randint(1, 255))
#    cor = (r_color, g_color, b_color)
#    return cor
#
#def desenhar_circulos_espiral(tamanho_circulo):
#    ''' Loop para reproduzir o espiral em circulos '''
#    for _ in range(int(360/tamanho_circulo)):
#        tartaruga.speed("fastest")
#        tartaruga.color(cor_aleatoria())
#        tartaruga.circle(100)
#        tartaruga.setheading(tartaruga.heading() + tamanho_circulo)
#
#desenhar_circulos_espiral(5)

# Fazendo uma obra de arte
lista_de_cores = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124),
(172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35),
(145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50),
(183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64),
(30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

tartaruga.penup()
tartaruga.hideturtle()
tartaruga.setheading(225)
tartaruga.forward(300)
tartaruga.setheading(0)

numeros_de_bolinhas = 100

for i in range(1, numeros_de_bolinhas + 1):
    tartaruga.dot(20, random.choice(lista_de_cores))
    tartaruga.forward(50)

    if i % 10 == 0:
        tartaruga.setheading(90)
        tartaruga.forward(50)
        tartaruga.setheading(180)
        tartaruga.forward(500)
        tartaruga.setheading(0)


cenario.exitonclick()
