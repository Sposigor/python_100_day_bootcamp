''' Exercicio do dia 19 '''

from turtle import Turtle, Screen
import random

# Objeto da classe Screen
cenario = Screen()
cenario.setup(width=500, height=400)


# Variáveis
resposta_usuario = cenario.textinput(title="Bem vindo a Velozes e Furiosos - THE TURTLE",
                                    prompt="Digite a cor da tartaruga que vai vencer o jogo: ")
y_posições = [-70, -40, -10, 20, 50, 80]
cores = ['red', 'blue', 'green', 'orange', 'purple', 'pink']
a_corrida_esta_acabando = False
if resposta_usuario:
    a_corrida_esta_acabando = True
todas_as_tartarugas = []

# Estancia da classe Turtle
for i in range(0, 6):
    Web = Turtle('turtle')
    Web.color(cores[i])
    Web.penup()
    Web.goto(x=-225, y=y_posições[i])
    todas_as_tartarugas.append(Web)

while a_corrida_esta_acabando:

    for tartaruga in todas_as_tartarugas:
        if tartaruga.xcor() > 190:
            a_corrida_esta_acabando = False
            vencedor = tartaruga.pencolor()
            if resposta_usuario == vencedor:
                print(f'Parabéns, a tartaruga {vencedor} venceu a corrida!')
            else:
                print(f'Você perdeu, a tartaruga que venceu é {vencedor}')

        andar_tartaruga = random.randint(0, 10)
        tartaruga.forward(andar_tartaruga)



cenario.exitonclick()
