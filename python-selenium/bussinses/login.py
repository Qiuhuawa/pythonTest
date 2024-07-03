import os
import time
from selenium.webdriver.common.by import By
import yaml

path = os.getcwd()
from util import log


class login:
    def __init__(self, driver):
        self.driver = driver
        self.logs = log.log_message()
        self.file = open(path + "\\data\\page_data.yaml", "r", encoding="UTF-8")
        self.data = yaml.load(self.file, Loader=yaml.FullLoader)
        self.file.close()
        self.lo_url = self.data['login'].get('url')
        self.username = self.data['login'].get('name')
        self.password = self.data['login'].get('password')
        self.sub = self.data['login'].get('login_bt')
        self.driver.get(self.lo_url)

    def login(self, name, password):
        try:
            self.driver.find_element(By.ID, self.username).send_keys(name)
            self.driver.find_element(By.ID, self.password).send_keys(password)
            self.driver.find_element(By.ID, self.sub).click()
        except Exception as e:
            e.with_traceback()
