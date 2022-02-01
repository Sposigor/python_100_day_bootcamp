"""
Exercicio dia 56
"""

from distutils.log import debug
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    """ Pagina inicial """
    return render_template("index2.html")


if __name__ == '__main__':
    app.run(debug=True)