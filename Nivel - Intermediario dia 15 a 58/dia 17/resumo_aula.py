''' Continuação do entedimento do POO, dia 17 '''

class Usuario:
    ''' classe para o usuario '''
    def __init__(self, nome, email, senha):
        ''' inicializa os atributos '''
        self.nome = nome
        self.email = email
        self.senha = senha

    def __str__(self):
        ''' metodo str para print '''
        return f'Nome: {self.nome}\nEmail: {self.email}\nSenha: {self.senha}'

igor = Usuario('Igor', 'igor@igor', '123')
print(igor)
