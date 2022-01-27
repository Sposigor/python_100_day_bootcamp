"""
Exercicios do dia 48

Vamos usar o Selenium para automatizar alguns processos na internet.

"""


from selenium import webdriver

CHROMIUM_DRIVER_PATH = r'/usr/lib/chromium/chromedriver'

driver = webdriver.Chrome(executable_path=CHROMIUM_DRIVER_PATH)

driver.maximize_window()
driver.get('https://www.python.org/')


eventos_datas = driver.find_elements_by_css_selector(".event-widget time")
eventos_descrição = driver.find_elements_by_css_selector(".event-widget li a")
eventos = {}


# Tentei usar enumerate, mas não consegui.
for x in range(len(eventos_datas)):
    eventos[x] = {
        "data": eventos_datas[x].text,
        "nome": eventos_descrição[x].text
    }

print(eventos)

driver.quit()
