from turtle import Turtle, Screen
import outro_modulo
print(outro_modulo.variavel)

destroy = Turtle()
print(destroy)
destroy.shape('turtle')
destroy.color('red')
destroy.speed(1)
destroy.forward(100)

tela = Screen()
print(tela.canvheight)
tela.exitonclick()
