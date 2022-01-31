""" 
Exercicio dia 54 

"""

from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return '<h1>Olá mundo!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
