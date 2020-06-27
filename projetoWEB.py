from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as CondicaoExperada
from selenium.webdriver.common.keys import Keys
import time
import random
class projetoWEB:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', options=chrome_options)
        self.wait = WebDriverWait(
            driver=self.driver,
            timeout=10,
            poll_frequency=1,
            ignored_exceptions=[NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException]
        )
    def Iniciar(self):
        self.driver.get('https://cursoautomacao.netlify.com')
        self.radio_btns()
        self.campo_digitar()
        self.acessos()
        print("Finalizando o programa")
        time.sleep(3)
    
    def radio_btns(self):
        try:
            escolha_rbtn = str(input("Qual opção de sistema operacional marcar? "))
            opcoes = self.wait.until(CondicaoExperada.element_to_be_clickable(
                    (By.XPATH, f'//input[@value="{escolha_rbtn}"]')
            )
            )
            opcoes.click()
        except Exception:
            print("Por favor escolha uma opção entre [Windows 10, Linux, Mac]")
            self.radio_btns()  


    def campo_digitar(self):
        try:
            texto_usuario = str(input("Qual texto quer digitar? "))
            textarea = self.wait.until(CondicaoExperada.element_to_be_clickable(
                (By.XPATH, '//textarea[@placeholder="digite seu texto aqui"]')
            )
            )
            textarea.click()
            for letra in texto_usuario:
                textarea.send_keys(letra)
                time.sleep(random.randint(1,5) / 30)       
        except Exception:
            print("Ocorreu um erro. Tente Novamente")
            self.campo_digitar()


    
    def acessos(self):
        try:
            escolha_acesso = input(
                'Quais acessos devem ser liberados? * Caso queira liberar mais de um acesso, informe os niveis separados por vírgula. ')
            niveis = escolha_acesso.split(',')
            for nivel in niveis:
                liberar_nivel = self.wait.until(CondicaoExperada.element_to_be_clickable(
                    (By.XPATH, f'//input[@id="acessoNivel{nivel}Checkbox"]')
            )
            )
                liberar_nivel.click()
        except Exception:
            print('Ocorreu um erro digite o nivel de acesso entre virgula.')
            self.Acesso()
            
root = projetoWEB()
root.Iniciar()