''' Exercicio dia 34 '''

from modelo_da_questao import Questão
from dados import questão
from mecanismo_pergunta import MecanismoPergunta
from ui import InterfaceJogo

banco_questão = []
for perguntas in questão:
    pergunta_texto = perguntas["question"]
    pergunta_resposta = perguntas["correct_answer"]
    nova_pergunta = Questão(pergunta_texto, pergunta_resposta)
    banco_questão.append(nova_pergunta)


jogo = MecanismoPergunta(banco_questão)
UI_do_jogo = InterfaceJogo(jogo)
