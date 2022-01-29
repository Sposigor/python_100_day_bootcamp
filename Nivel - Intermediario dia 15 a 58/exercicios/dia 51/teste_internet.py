"""
Exercicio do dia 51

"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import geckodriver_autoinstaller

geckodriver_autoinstaller.install()


class TesteInternet:
    """ Class para verificar a velocidade da internet usando o selenium """

    def __init__(self):
        """ Inicializa a classe e alguns atributos """
        self.subir = 0
        self.baixar = 0
        self.driver = self.driver_firefox()

    def driver_firefox(self):
        """ Inicializa o driver """
        perfil = webdriver.FirefoxProfile(r'/home/sposigor/.mozilla/firefox/r8glg5zc.default-release/')
        perfil.update_preferences()
        desired = DesiredCapabilities.FIREFOX
        driver = webdriver.Firefox(firefox_profile=perfil,
                                    desired_capabilities=desired)
        return driver

    def pegar_velocidade_net(self):
        """ Retorna a velocidade da internet """
        self.driver.get("https://www.speedtest.net/")

        go_btn: WebElement = self.driver.find_element(By.CLASS_NAME, 'js-start-test')
        go_btn.click()

        sleep(45)
        self.subir = float(self.driver.find_element(By.CLASS_NAME, 'upload-speed').text)
        self.baixar = float(self.driver.find_element(By.CLASS_NAME, 'download-speed').text)

    def envinado_messagem_twiter(self):
        """ Envia a mensagem no twitter """
        texto = f'Velocidade da internet: {self.subir} Mbps de upload e {self.baixar} Mbps de download'

        self.driver.get("https://twitter.com/")
        self.driver.maximize_window()

        # Indo para posição 0, 0 da pagina
        ação = ActionChains(self.driver)
        sleep(2)
        ação.move_to_element_with_offset(self.driver.find_element_by_tag_name('body'), 0,0)

        # Indo até o botão de login
        sleep(2)
        ação.move_by_offset(xoffset=250, yoffset=270).click().perform()

        # Selecionando login com google
        sleep(8)
        ação.move_by_offset(xoffset=-350, yoffset=-425).click().perform()

        # Selecionando a guia do navegador, no meu caso tem uma guia fixada, aumentando a quantidade em 1
        sleep(2)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[2])

        # Usando o login do google
        sleep(2)
        login: WebElement = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/main/div/div/div[1]/div[1]')
        login.click()

        # Retornando a guia do navegador para o twitter
        self.driver.switch_to.window(handles[1])

        # Selecionando a caixa de texto e enviando a mensagem
        sleep(5)
        ação.move_by_offset(xoffset=800, yoffset=80).click().send_keys(texto).perform()

        # Usando o botão de enviar
        sleep(2)
        ação.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()


        # Saindo da conta do twitter
        sleep(5)
        ação.move_by_offset(xoffset=-350, yoffset=840).click().perform()
        sleep(1)
        ação.move_by_offset(xoffset=0, yoffset=-60).click().perform()
        sleep(1)
        ação.move_by_offset(xoffset=480, yoffset=-320).click().perform()

        # Fechando o navegador
        self.driver.quit()
