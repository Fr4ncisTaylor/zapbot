from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
from time import sleep
import config

os.system('rm -rf profile')
class bot:
    # O local de execução do nosso script
    dir_path = os.getcwd()
    # O caminho do chromedriver
    chromedriver = config.path#os.path.join(dir_path, "chromedriver")
    # Caminho onde será criada pasta profile
    profile = os.path.join(dir_path, "profile", "wpp")

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        # Configurando a pasta profile, para mantermos os dados da seção
        self.options.add_argument(
            r"user-data-dir={}".format(self.profile))
        # Inicializa o webdriver
        self.driver = webdriver.Chrome(
            self.chromedriver, chrome_options=self.options)
        # Abre o whatsappweb
        self.driver.get(config.webWhatsapp)
        # Aguarda alguns segundos para validação manual do QrCode
        self.driver.implicitly_wait(15)

    def leftMessage(self):
        """ Captura a ultima mensagem da conversa """
        try:
            post = self.driver.find_elements_by_class_name(config.classes['msg_text'])
            ultimo = len(post) - 1
            # O texto da ultima mensagem
            texto = post[ultimo].find_element_by_css_selector(config.css['left_msg']).text
            return texto
        except Exception as e:
            print("Erro ao ler msg, tentando novamente!")

    def sendMessage(self, msg):
        """ Envia uma mensagem para a conversa aberta """
        try:
            sleep(2)
            # Seleciona acaixa de mensagem
            self.caixa_de_mensagem = self.driver.find_element_by_class_name(config.classes['msg_box'])
            # Digita a mensagem
            #self.caixa_de_mensagem.send_keys(msg)
            for part in msg.split('\n'):
                self.caixa_de_mensagem.send_keys(part)
                ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
            sleep(1)
            # Seleciona botão enviar
            self.botao_enviar = self.driver.find_element_by_class_name(config.classes['send_button'])
            # Envia msg
            self.botao_enviar.click()
            sleep(2)
        except Exception as e:
            print("Erro ao enviar msg", e)

    def sendMedia(self, fileToSend):
        """ Envia media """
        try:
            # Clica no botão adicionar
            self.driver.find_element_by_css_selector(config.css['media_button']).click()
            # Seleciona input
            attach = self.driver.find_element_by_css_selector(config.css['media_input'])
            # Adiciona arquivo
            attach.send_keys(fileToSend)
            sleep(3)
            # Seleciona botão enviar
            send = self.driver.find_element_by_xpath(config.css['send_button'])
            # Clica no botão enviar
            send.click()
        except Exception as e:
            print("Erro ao enviar media", e)

    def initialize(self, contato):
        """ Abre a conversa com um contato especifico """
        try:
            # Seleciona a caixa de pesquisa de conversa
            self.caixa_de_pesquisa = self.driver.find_element_by_class_name(config.classes['search_box'])#
            # Digita o nome ou numero do contato
            self.caixa_de_pesquisa.send_keys(contato)
            sleep(2)
            # Seleciona o contato
            self.contato = self.driver.find_element_by_xpath("//span[@title = '{}']".format(contato))
            # Entra na conversa
            self.contato.click()
        except Exception as e:
            raise e

    def loop(self,handle):
        msg = ""
        left_msg = ""
        while msg != "/quit":
            msg = bot.leftMessage(self)
            if left_msg != msg:
                handle(msg)
            left_msg = msg
            sleep(2)
