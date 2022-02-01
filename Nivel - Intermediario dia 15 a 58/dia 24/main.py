''' Exercicio do dia 24 '''

import os

# PATH
carta = os.path.abspath('Nivel - Intermediario dia 15 a 58\exercicios\dia 24\input\carta\carta_inicial.txt')
lista_nome = os.path.abspath(r'Nivel - Intermediario dia 15 a 58\exercicios\dia 24\input\lista_nomes\nomes_selecionados.txt')
resultado = os.path.abspath(r'Nivel - Intermediario dia 15 a 58\exercicios\dia 24\output\pronto_para_envio')


# Variáveis
troca_nome = "[nome]"

# Abrindo os arquivos

with open(lista_nome, 'r', encoding='utf-8') as arquivo_lista:
    nomes_selecionados = arquivo_lista.readlines()

with open(carta, 'r', encoding='utf-8') as arquivo_carta:
    carta_inicial = arquivo_carta.read()
    # Salvanto a nova carta com os nomes de cada participante
    for nome in nomes_selecionados:
        nomes_stripped = nome.strip()
        nova_carta = carta_inicial.replace(troca_nome, nomes_stripped)
        with open(f"{resultado}\{nomes_stripped}.txt", 'w', encoding='utf-8') as arquivo_novo:
            arquivo_novo.write(nova_carta)
