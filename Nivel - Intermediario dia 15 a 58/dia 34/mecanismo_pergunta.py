''' Exercicio dia 34 '''

import html

class MecanismoPergunta:
    ''' Mecanismo das perguntas '''
    def __init__(self, lista_da_questão):
        ''' Inicialização do mecanismo '''
        self.numero_questão = 0
        self.placar = 0
        self.lista_questão = lista_da_questão
        self.questão_atual = None

    def ainda_tem_pergunta(self):
        ''' Verificar se ainda tem perguntas '''
        return self.numero_questão < len(self.lista_questão)

    def nova_questão(self):
        ''' Faz a proxima pergunta '''
        self.questão_atual = self.lista_questão[self.numero_questão]
        self.numero_questão += 1
        texto_pergunta = html.unescape(self.questão_atual.texto)
        return f"P.{self.numero_questão}: {texto_pergunta}"

    def check_pergunta(self, resposta_usuario):
        ''' Valida se a resposta do usuario está correta '''
        resposta_correta = self.questão_atual.resposta
        if resposta_usuario.lower() == resposta_correta.lower():
            self.placar += 1
            return True
        else:
            return False
