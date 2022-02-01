"""
Exercicio do dia 55
"""

import random
from distutils.log import debug
from flask import Flask

numero_aleatorio = random.randint(1, 10)


app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    """ Pagina inicial """
    return '<h1>Selecione o numero entre 1 a 10</h1>' \
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" />'


@app.route("/<int:numero>")
def escolha_usuario(numero):
    """ Escolha do usuario """
    if numero > numero_aleatorio:
        return '<h1 style="color: purple">Voce errou, o numero sorteado é menor</h1>' \
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif numero < numero_aleatorio:
        return '<h1 style="color: red">Voce errou, o numero sorteado é maior</h1>' \
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"

    else:
        return '<h1 style="color: blue">Voce acertou</h1>' \
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"



if __name__ == '__main__':
    app.run(debug=True)
