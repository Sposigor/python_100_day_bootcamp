''' Exercicio do dia 19 '''

from turtle import Turtle, Screen

# Objeto
tartaruga = Turtle()

# Metodos do objeto
tartaruga.shape('turtle')
tartaruga.screen.bgcolor('black')
tartaruga.color('white')
tartaruga.pensize(2)

# Funções de movimento e limpeza do quadro
def f_frente():
    ''' Vai para frente '''
    tartaruga.forward(10)

def f_esquerda():
    ''' Vai para esquerda '''
    novo_angulo = tartaruga.heading() + 10
    tartaruga.setheading(novo_angulo)

def f_direita():
    ''' Vai para direita '''
    novo_angulo = tartaruga.heading() - 10
    tartaruga.setheading(novo_angulo)

def f_tras():
    ''' Vai para tras '''
    tartaruga.backward(10)

def limpar_tela():
    ''' Limpa a tela '''
    tartaruga.clear()
    tartaruga.penup()
    tartaruga.home()
    tartaruga.pendown()

# Metodo do cenario
cenario = Screen()

cenario.listen()
cenario.onkey(fun=f_frente, key='w')
cenario.onkey(fun=f_esquerda, key='a')
cenario.onkey(fun=f_direita, key='d')
cenario.onkey(fun=f_tras, key='s')
cenario.onkey(fun=limpar_tela, key='c')

cenario.exitonclick()
