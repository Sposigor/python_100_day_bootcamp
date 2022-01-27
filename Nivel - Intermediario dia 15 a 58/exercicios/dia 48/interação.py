"""
Exercicios do dia 48

Vamos usar o Selenium para automatizar alguns processos na internet.

"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

CHROMIUM_DRIVER_PATH = r'/usr/lib/chromium/chromedriver'

driver = webdriver.Chrome(executable_path=CHROMIUM_DRIVER_PATH)

driver.maximize_window()
driver.get('https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal')

pesquisa = driver.find_element_by_name('search')
pesquisa.send_keys('Python')
pesquisa.send_keys(Keys.ENTER)


driver.quit()
