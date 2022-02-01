"""
Exercicio do dia 50

"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

EMAIL = 'email'
SENHA = 'senha'
CHROMIUM_DRIVER_PATH = r'/usr/lib/chromium/chromedriver'


driver = webdriver.Chrome(CHROMIUM_DRIVER_PATH)
opções = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=driver, options=opções)

driver.get('https://tinder.com/app/recs')
time.sleep(2)
tela_login = driver.find_element(By.CLASS_NAME, 'button')
tela_login.click()
time.sleep(1)
login_facebook = driver.find_element(By.XPATH, '//*[@id="q36386411"]/div/div/div[1]/div/div[3]/span/div[2]/button')
login_facebook.click()
time.sleep(2)
tela_tinder = driver.window_handles[0]
facebook_tela = driver.window_handles[1]
driver.switch_to.window(facebook_tela)
time.sleep(1)
email = driver.find_element(By.XPATH, '//*[@id="email"]')
email.send_keys(EMAIL)
senha = driver.find_element(By.XPATH, '//*[@id="pass"]')
senha.send_keys(SENHA)
tela_login = driver.find_element(By.ID, 'loginbutton')
tela_login.submit()
driver.switch_to.window(tela_tinder)
time.sleep(6)
tinder_ok = driver.find_element(By.XPATH, '//*[@id="q36386411"]/div/div/div/div/div[3]/button[1]')
tinder_ok.click()
tinder_msg = driver.find_element(By.XPATH, '//*[@id="q36386411"]/div/div/div/div/div[3]/button[1]')
tinder_msg.click()
while True:
    time.sleep(2)
    try:
        ação = ActionChains(driver)
        ação.send_keys(Keys.ARROW_RIGHT)
        ação.perform()
    except:
        print("Erro")
        driver.quit()
