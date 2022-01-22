''' Exercicio dia 33 '''

from datetime import datetime
import smtplib
import time
import requests


meu_email = ""
minha_senha = ""
minha_latitude = -23.533773
minha_longitude = -46.625290


def perguntando_pra_iss_aonde_ela_esta():
    ''' Descobrindo via API aonde está a ISS '''
    resposta = requests.get(url="http://api.open-notify.org/iss-now.json")
    resposta.raise_for_status()
    dados = resposta.json()

    iss_latitude = float(dados["iss_position"]["latitude"])
    iss_longitude = float(dados["iss_position"]["longitude"])

    # Sua posição com uma diferença de 5 +- graus de diferença da posição da ISS
    if minha_latitude-5 <= iss_latitude <= minha_latitude+5 and minha_longitude-5 <= iss_longitude <= minha_longitude+5:
        return True


def esta_de_noite():
    ''' Verificando que horas escurece para da mais visibilidade para ISS '''
    parametros = {
        "lat": minha_latitude,
        "lng": minha_longitude,
        "formatted": 0,
    }
    resposta = requests.get("https://api.sunrise-sunset.org/json", params=parametros)
    resposta.raise_for_status()
    dados = resposta.json()
    nascer_do_sol = int(dados["results"]["sunrise"].split("T")[1].split(":")[0])
    por_do_sol = int(dados["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= por_do_sol or time_now <= nascer_do_sol:
        return True


while True:
    time.sleep(60)
    if perguntando_pra_iss_aonde_ela_esta() and esta_de_noite():
        connection = smtplib.SMTP("")
        connection.starttls()
        connection.login(meu_email, minha_senha)
        connection.sendmail(
            from_addr=meu_email,
            to_addrs=minha_senha,
            msg="Assunto:Olhe para cima, a ISS está passando por você!\n\n"
        )
