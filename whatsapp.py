from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
from time import sleep
import config

os.system('rm -rf profile') # REMOVE OLD PROFILE

class bot:
    dir_path = os.getcwd()
    chromedriver = config.path
    profile = os.path.join(dir_path, "profile", "wpp")

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(
            r"user-data-dir={}".format(self.profile))
        # start webdriver
        self.driver = webdriver.Chrome(
            self.chromedriver, chrome_options=self.options)
        self.driver.get(config.webWhatsapp)
        self.driver.implicitly_wait(15)

    def leftMessage(self):
        try:
            post = self.driver.find_elements_by_class_name(config.classes['msg_text'])
            ultimo = len(post) - 1
            texto = post[ultimo].find_element_by_css_selector(config.css['left_msg']).text
            return texto
        except Exception as e:
            print("Error getting message")

    def sendMessage(self, msg):
        try:
            sleep(2)
            # select box message and typing
            self.caixa_de_mensagem = self.driver.find_element_by_class_name(config.classes['msg_box'])
            for part in msg.split('\n'):
                self.caixa_de_mensagem.send_keys(part)
                ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
            sleep(1)
            # Select send button
            self.botao_enviar = self.driver.find_element_by_class_name(config.classes['send_button'])
            # click
            self.botao_enviar.click()
            sleep(2)
        except Exception as e:
            print("Error send message", e)
    def sendMedia(self, file):
        try:
            self.driver.find_element_by_css_selector(config.css['media_button']).click()
            attach = self.driver.find_element_by_css_selector(config.css['media_input'])
            attach.send_keys(fileToSend)
            sleep(3)
            send = self.driver.find_element_by_xpath(config.css['send_button'])
            send.click()
        except Exception as e:
            print("Error send media", e)

    def initialize(self):
        contato = config.contact
        """ Open especific contact """
        try:
            self.caixa_de_pesquisa = self.driver.find_element_by_class_name(config.classes['search_box'])#
            self.caixa_de_pesquisa.send_keys(contato)
            sleep(2)
            self.contato = self.driver.find_element_by_xpath("//span[@title = '{}']".format(contato))
            self.contato.click()
        except Exception as e:
            raise e

    def loop(self,handle):
        msg = ""
        left_msg = ""
        while 1==1:
            msg = bot.leftMessage(self)
            if left_msg != msg:
                handle(msg)
            left_msg = msg
            sleep(2)
