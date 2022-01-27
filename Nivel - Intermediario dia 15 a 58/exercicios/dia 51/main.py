"""
Exercicio do dia 51

"""


from selenium import webdriver


EMAIL = 'email'
SENHA = 'senha'
CHROMIUM_DRIVER_PATH = r'/usr/lib/chromium/chromedriver'


opções = webdriver.ChromeOptions()
driver = webdriver.Chrome(CHROMIUM_DRIVER_PATH, options=opções)
