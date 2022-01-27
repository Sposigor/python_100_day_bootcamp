"""
Exercicio do dia 49

Vamos usar o bot para aplicar em empregos no linkedin

"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


CONTA_EMAIL = "EMAIL DE LOGIN"
CONTA_SENHA = "SENHA DA CONTA"
NUMERO_TELEFONE = "NUMERO DE TELEFONE"
CHROMIUM_DRIVER_PATH = r'/usr/lib/chromium/chromedriver'


driver = webdriver.Chrome(CHROMIUM_DRIVER_PATH)
driver.get("https://www.linkedin.com/jobs/search?keywords=Python&location=S%C3%A3o%20Paulo%2C%20S%C3%A3o%20Paulo%2C%20Brasil&geoId=104746682&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")

time.sleep(2)
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(5)
campo_email = driver.find_element_by_id("username")
campo_email.send_keys(CONTA_EMAIL)
campo_senha = driver.find_element_by_id("password")
campo_senha.send_keys(CONTA_SENHA)
campo_senha.send_keys(Keys.ENTER)

time.sleep(5)

lista_vagas = driver.find_elements_by_css_selector(".job-card-container--clickable")

for lista in lista_vagas:
    print("called")
    lista.click()
    time.sleep(2)

    # Localizar o botão de aplicar
    try:
        aplicar_botão = driver.find_element_by_css_selector(".jobs-s-apply button")
        aplicar_botão.click()
        time.sleep(5)

        # Se o campo telefone estiver vazio
        telefone = driver.find_element_by_class_name("fb-single-line-text__input")
        if telefone.text == "":
            telefone.send_keys(NUMERO_TELEFONE)

        botão_envio = driver.find_element_by_css_selector("footer button")

        # Se o processo precisar de mais etapas para finalizar a aplicação
        if botão_envio.get_attribute("data-control-name") == "continue_unify":
            fecha_botão = driver.find_element_by_class_name("artdeco-modal__dismiss")
            fecha_botão.click()
            time.sleep(2)
            descartar_botão = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            descartar_botão.click()
            print("Aplicação complexa, finalizada")
            continue
        else:
            botão_envio.click()

        # Aplicação concluida, fecha o pop-up
        time.sleep(2)
        fecha_botão = driver.find_element_by_class_name("artdeco-modal__dismiss")
        fecha_botão.click()

    # Se aplicou em todas as possibilidade
    except NoSuchElementException:
        print("Sem botão para aplicar")
        continue

time.sleep(5)
driver.quit()
