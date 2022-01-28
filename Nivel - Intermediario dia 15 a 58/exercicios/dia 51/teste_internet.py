"""
Exercicio do dia 51

"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import geckodriver_autoinstaller

geckodriver_autoinstaller.install()


class TesteInternet:
    """ Class para verificar a velocidade da internet usando o selenium """

    def __init__(self):
        """ Inicializa a classe e alguns atributos """
        self.subir = 0
        self.descer = 0
        self.driver = self.driver_firefox()


    def driver_firefox(self):
        """ Inicializa o driver """
        perfil = webdriver.FirefoxProfile(r'/home/sposigor/.mozilla/firefox/3boritwh.bot/')
        perfil.set_preference("dom.webdriver.enabled", False)
        perfil.set_preference('useAutomationExtension', False)
        perfil.update_preferences()
        desired = DesiredCapabilities.FIREFOX
        driver = webdriver.Firefox(firefox_profile=perfil,
                                    desired_capabilities=desired)
        return driver

    def get_velocidade_net(self):
        """ Retorna a velocidade da internet """
        self.driver.get("https://www.speedtest.net/")

        go_btn: WebElement = self.driver.find_element(By.CLASS_NAME, 'js-start-test')
        go_btn.click()

        sleep(45)
        self.subir = float(self.driver.find_element(By.CLASS_NAME, 'upload-speed').text)
        self.descer = float(self.driver.find_element(By.CLASS_NAME, 'download-speed').text)
        self.driver.close()

    def envinado_messagem_twiter(self):
        """ Envia a mensagem no twitter """
        texto = f'Velocidade da internet: {self.subir} Mbps de upload e {self.descer} Mbps de download'
        self.driver.get("https://twitter.com/")
        sleep(3)
        mouse = ActionChains(self.driver)
        mouse.move_by_offset(150, -300).click()








bot = TesteInternet()
bot.envinado_messagem_twiter()
