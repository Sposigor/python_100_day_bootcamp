"""
Exercicio dia 57
"""


class Post:
    """ Classe para retorna o post """
    def __init__(self, post_id, titulo, subtitulo, body):
        self.id = post_id
        self.titulo = titulo
        self.subtitulo = subtitulo
        self.body = body
