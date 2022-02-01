"""
Exercicios do dia 48

Vamos usar o Selenium para automatizar alguns processos na internet.

"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

CHROMIUM_DRIVER_PATH = r'/usr/lib/chromium/chromedriver'

driver = webdriver.Chrome(executable_path=CHROMIUM_DRIVER_PATH)

driver.maximize_window()
driver.get('https://secure-retreat-92358.herokuapp.com/')

primeiro_nome = driver.find_element_by_name('fName')
primeiro_nome.send_keys('Igor')

segundo_nome = driver.find_element_by_name('lName')
segundo_nome.send_keys('Esposito')

email = driver.find_element_by_name('email')
email.send_keys('sposigor@gmail.com')


# botão metodo xpath
botão = driver.find_element_by_xpath("/html/body/form/button")
botão.send_keys(Keys.ENTER)

# botão metodo css selector
# botão = driver.find_element_by_css_selector("form button")
# botão.click()
