"""
Exercicio do dia 47

"""

import smtplib
import requests
from bs4 import BeautifulSoup


# Variaveis
URL = "https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B075CWJ3T8"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

SMTP_ENDEREÇO = "smtp.gmail.com"
EMAIL = 'segredo'
SENHA = 'segredo'

# Resposta do request
respostas = requests.get(URL, headers=header)
dump = respostas.text

# BS4 fazendo magica
sopa = BeautifulSoup(dump, "lxml")
preço_xml = sopa.find("span", class_="apexPriceToPay")
preço = preço_xml.find("span", class_="a-offscreen").getText().strip("$")

# Enviando email quando o valor chegar no valor desejado

titulo = sopa.find(id="productTitle").get_text().strip()

PREÇO_COMPRA = 100

if preço < PREÇO_COMPRA:
    MENSSAGEM = f"{titulo} está com o valor de USD:{PREÇO_COMPRA}"

    with smtplib.SMTP(SMTP_ENDEREÇO, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, SENHA)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Assunto: Alerta de Preços!\n\n{MENSSAGEM}\n{URL}"
        )
