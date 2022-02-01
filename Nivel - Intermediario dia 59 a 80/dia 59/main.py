from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/5a3a9de6f82459b61269").json()

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    """ Retorna all posts """
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    """ Mostrar os blogs """
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    """ Mostrar a pagina sobre """
    return render_template("about.html")


@app.route("/contact")
def contact():
    """ Mostrar a pagina de contato """
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
