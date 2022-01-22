''' Exercicio do dia 32 '''

from datetime import datetime
import pandas
import random
import smtplib

email = "Seu Email"
senha = "Sua Senha"

agora = datetime.now()
agora_tupla = (agora.month, agora.day)

dados = pandas.read_csv("aniversario.csv")
dicionario_niver = {(dados_row["mes"], dados_row["dia"]): dados_row for (index, dados_row) in dados.iterrows()}
if agora_tupla in dicionario_niver:
    pessoa_niver = dicionario_niver[agora_tupla]
    path_arquivo = f"cartas_templates/carta_{random.randint(1,3)}.txt"
    with open(path_arquivo) as carta:
        conteudo = carta.read()
        conteudo = conteudo.replace("[NOME]", pessoa_niver["name"])

    with smtplib.SMTP("provedor do seu email") as connection:
        connection.starttls()
        connection.login(email, senha)
        connection.sendmail(
            from_addr=email,
            to_addrs=pessoa_niver["email"],
            msg=f"Assunto:Feliz Niver!\n\n{conteudo}"
        )
