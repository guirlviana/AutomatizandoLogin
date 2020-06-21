from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class automacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe',options=chrome_options)
        
    def Login(self):
        meu_email = 'aaaa@gmail.com'
        minhasenha = '1234'
        self.driver.get('http://colegiodomfelipe.eadbox.com/login')
        sleep(2)
        usuario = self.driver.find_element_by_id('user_email')
        usuario.send_keys(meu_email)
        sleep(2)
        senha = self.driver.find_element_by_id('user_password')
        senha.send_keys(minhasenha)
        sleep(1)
        botao_entrar = self.driver.find_element_by_class_name('btn.btn-success.btn-block.login-button')
        sleep(1)
        botao_entrar.click()

root = automacao()
root.Login()
