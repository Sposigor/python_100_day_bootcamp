"""
Exercicios do dia 48

Vamos usar o Selenium para automatizar alguns processos na internet.

"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

CHROMIUM_DRIVER_PATH = r'/usr/lib/chromium/chromedriver'

driver = webdriver.Chrome(executable_path=CHROMIUM_DRIVER_PATH)

driver.maximize_window()
driver.get('http://orteil.dashnet.org/experiments/cookie/')

biscoito = driver.find_element(By.ID,'cookie')

AGORA = time.time()
CINCO_MINUTOS = AGORA + 300
TEMPO = 1


while time.time() < CINCO_MINUTOS:
    TEMPO_CINCO_SEGUNDOS = time.time() + TEMPO

    while time.time() < TEMPO_CINCO_SEGUNDOS:
        biscoito.click()
    DINHEIRO = int(driver.find_element(By.ID, 'money').text.replace(',',''))

    DIFERENÇA_MINIMA = DINHEIRO
    COMPRA_ITEM = ''
    COMPRA_CUSTO = 0

    MOUSE_APERTA = driver.find_element(By.ID, 'buyCursor')
    VOVOZINHA = driver.find_element(By.ID,'buyGrandma')
    FABRICA = driver.find_element(By.ID,'buyFactory')
    MINA = driver.find_element(By.ID,'buyMine')
    BARCO = driver.find_element(By.ID,'buyShipment')
    ALQUIMIA = driver.find_element(By.ID,'buyAlchemy lab')
    PORTAL = driver.find_element(By.ID,'buyPortal')
    MAQUINA_DO_TEMPO = driver.find_element(By.ID,'buyTime machine')

    ARMAZEM_CLICK = {
        'cursor':MOUSE_APERTA,
        'grandma':VOVOZINHA,
        'factory':FABRICA,
        'mine':MINA,
        'shipment':BARCO,
        'alchemy':ALQUIMIA,
        'portal':PORTAL,
        'timemachine':MAQUINA_DO_TEMPO
    }

    MOUSE_CUSTO = int(driver.find_element(By.ID, 'buyCursor').text.split('-')[1].split()[0].strip().replace(',', ''))
    VOVOZINHA_CUSTO = int(driver.find_element(By.ID, 'buyGrandma').text.split('-')[1].split()[0].strip().replace(',', ''))
    FABRICA_CUSTO = int(driver.find_element(By.ID, 'buyFactory').text.split('-')[1].split()[0].strip().replace(',', ''))
    MINA_CUSTO = int(driver.find_element(By.ID, 'buyMine').text.split('-')[1].split()[0].strip().replace(',', ''))
    BARCO_CUSTO = int(driver.find_element(By.ID, 'buyShipment').text.split('-')[1].split()[0].strip().replace(',', ''))
    ALQUIMIA_CUSTO = int(driver.find_element(By.ID, 'buyAlchemy lab').text.split('-')[1].split()[0].strip().replace(',', ''))
    PORTAL_CUSTO = int(driver.find_element(By.ID, 'buyPortal').text.split('-')[1].split()[0].strip().replace(',', ''))
    MAQUINA_DO_TEMPO_CUSTO = int(driver.find_element(By.ID, 'buyTime machine').text.split('-')[1].split()[0].strip().replace(',', ''))

    ARMAZEM_CUSTO = {
        'cursor':MOUSE_CUSTO,
        'grandma':VOVOZINHA_CUSTO,
        'factory':FABRICA_CUSTO,
        'mine':MINA_CUSTO,
        'shipment':BARCO_CUSTO,
        'alchemy':ALQUIMIA_CUSTO,
        'portal':PORTAL_CUSTO,
        'timemachine':MAQUINA_DO_TEMPO_CUSTO
    }

    for X in ARMAZEM_CUSTO.keys():
        DIFERENÇA = DINHEIRO - ARMAZEM_CUSTO[X]

        if DIFERENÇA < DIFERENÇA_MINIMA and DIFERENÇA >= 0:
            COMPRA_ITEM = X

    ARMAZEM_CLICK[COMPRA_ITEM].click()

    if time.time() >= CINCO_MINUTOS:
        BISCOISTO_POR_SEGUNDO = driver.find_element(By.ID,'cps').text
        print(BISCOISTO_POR_SEGUNDO)
        driver.quit()

    TEMPO +=1
