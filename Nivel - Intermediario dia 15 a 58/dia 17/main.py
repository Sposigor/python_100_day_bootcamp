''' Exercicio da aula 17 '''
from modelo_questoes import Questao
from data import questoes_dados
from questoes_jogo import Questões

banco_questoes = []

for i in questoes_dados:
    questão_texto = i["questões"]
    questão_resposta = i["questão_correta"]
    nova_questões = Questao(questão_texto, questão_resposta)
    banco_questoes.append(nova_questões)

jogo = Questões(banco_questoes)

while jogo.ainda_tem_pergunta():
    jogo.proxima_questao()


print("Fim do jogo!")
print(f"Sua pontuação foi: {jogo.pontuação}/{jogo.numero_q}")
