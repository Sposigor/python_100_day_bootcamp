''' Exercicio da aula 17 '''

class Questões:
    ''' Classe para o jogo '''
    def __init__(self, lista_q):
        ''' Inicialização dos atributos '''
        self.numero_q = 0
        self.pontuação = 0
        self.lista_questoes = lista_q

    def ainda_tem_pergunta(self):
        ''' Confirma se quer continuar o jogo '''
        return self.numero_q < len(self.lista_questoes)

    def proxima_questao(self):
        ''' Proxima questão do jogo '''
        questao_atual = self.lista_questoes[self.numero_q]
        self.numero_q += 1
        resposta_usuario = input(f"Q.{self.numero_q}: {questao_atual.pergunta} "
                                "(Verdade/Falso): ")
        self.verifica_resposta(resposta_usuario, questao_atual.resposta)

    def verifica_resposta(self, resposta_usuario, resposta_correta):
        ''' Verifica a resposta do usuario '''
        if resposta_usuario.lower() == resposta_correta.lower():
            self.pontuação += 1
            print("Você está certo!")
        else:
            print("Você está errado!")
        print(f"A resposta correta é: {resposta_correta}.")
        print(f"Sua Pontuação é: {self.pontuação}/{self.numero_q}")
        print("\n")
