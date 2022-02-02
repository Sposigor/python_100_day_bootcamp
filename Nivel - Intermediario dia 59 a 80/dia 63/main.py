"""
Exercicio do dia 63, está com um bug em db.session.add tem que resolver
"""

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livros.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Livro(db.Model):
    """ Cadastro de livros """
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(250), unique=True, nullable=False)
    autor = db.Column(db.String(250), nullable=False)
    avaliacao = db.Column(db.Float, nullable=False)

    def __repr__(self):
        """ Retorna o titulo do livro """
        return f'<Livro {self.titulo}>'

db.create_all()


@app.route('/')
def inicio():
    """ Página inicial """
    livros = db.session.query(Livro).all()
    return render_template('index.html', livros=livros)


@app.route("/add", methods=['POST', 'GET'])
def add():
    """ Adiciona um livro """
    if request.method == 'POST':
        novo_livro = {
            "titulo": request.form['titulo'],
            "autor": request.form['autor'],
            "avaliacao": request.form['avaliação']
        }
        db.session.add(novo_livro)
        db.session.commit()

        return redirect(url_for('inicio'))
    return render_template('add.html')


@app.route("/edit", methods=["GET", "POST"])
def edit():
    """ Edita um livro """
    if request.method == "POST":
        livro_id = request.form["id"]
        livro_update = Livro.query.get(livro_id)
        livro_update.avaliacao = request.form["avaliacao"]
        db.session.commit()
        return redirect(url_for('inicio'))
    livro_id = request.args.get('id')
    livro_selecionado = Livro.query.get(livro_id)
    return render_template("edit_avaliacao.html", livro=livro_selecionado)


@app.route("/delete")
def delete():
    livro_id = request.args.get('id')

    livro_deletado = Livro.query.get(livro_id)
    db.session.delete(livro_deletado)
    db.session.commit()
    return redirect(url_for('inicio'))

if __name__ == "__main__":
    app.run(debug=True)
