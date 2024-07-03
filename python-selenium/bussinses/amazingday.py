import os
import time
from selenium.webdriver.common.by import By
import yaml

path = os.getcwd()
from util import log


class Login_tes:  #登录模块封装
    def __init__(self, driver):  #
        self.driver = driver
        self.logs = log.log_message()
        self.file = open(path + "\\data\\page_data.yaml", "r", encoding="UTF-8")
        self.data = yaml.load(self.file, Loader=yaml.FullLoader)
        self.file.close()
        self.lo_url = self.data['login'].get('url')
        self.username = self.data['login'].get('name')
        self.password = self.data['login'].get('password')
        self.sub = self.data['login'].get('login_bt')
        self.lo_suc = self.data['login'].get('login_suc')
        self.result = self.data['login'].get('login_result')
        self.driver.get(self.lo_url)

    def login(self, suc, name, password):
        try:
            self.driver.find_element(By.ID, self.username).send_keys(name)
            self.driver.find_element(By.ID, self.password).send_keys(password)
            self.driver.find_element(By.ID, self.sub).click()
            if suc == '1':
                return self.lo_suc
            else:
                self.login_err = self.driver.find_element(By.ID, self.result).text
                return self.login_err
        except Exception as e:
            self.logs.error_log('用例执行失败，原因：%s' % e)
            self.driver.quit()


class User_tes:
    def __init__(self, driver):
        self.driver = driver
        self.logs = log.log_message()
        self.file1 = open(path + "\\data\\page_data.yaml", "r", encoding="UTF-8")
        self.data = yaml.load(self.file1, Loader=yaml.FullLoader)
        self.file1.close()
        self.flag = self.data['user'].get('user_flag')
        self.url = self.data['user'].get('url')
        self.depth1 = self.data['user'].get('user_depth1')
        self.depth2 = self.data['user'].get('user_depth2')
        self.menu = self.data['user'].get('user_drop')
        self.adduser = self.data['user'].get('user_add')
        self.account = self.data['user'].get('user_account')
        self.name = self.data['user'].get('user_name')
        self.userid = self.data['user'].get('user_id')
        self.email = self.data['user'].get('user_email')
        self.telephone = self.data['user'].get('user_phone')
        self.save = self.data['user'].get('user_save')
        self.fall1 = self.data['user'].get('user_fail1')
        self.fall2 = self.data['user'].get('user_fail2')
        self.fall3 = self.data['user'].get('user_fail3')
        self.fall4 = self.data['user'].get('user_fail4')
        self.table = self.data['user'].get('user_table')
        self.deflag = self.data['user'].get('user_deflag')
        self.deletuser = self.data['user'].get('user_delete')
        self.deletconf = self.data['user'].get('user_deletconf')
        self.driver.get(self.url)
        time.sleep(2)

    def add(self, suc, account, name, userid, email, telephone, gender):
        try:
            self.driver.find_element(By.XPATH, self.depth1).click()
            self.driver.find_element(By.XPATH, self.depth2).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.menu).click()
            self.driver.find_element(By.ID, self.adduser).click()
            time.sleep(1)
            self.driver.find_element(By.ID, self.account).send_keys(account)
            self.driver.find_element(By.ID, self.name).send_keys(name)
            self.driver.find_element(By.ID, self.userid).send_keys(userid)
            self.driver.find_element(By.ID, self.email).send_keys(email)
            self.driver.find_element(By.ID, self.telephone).send_keys(telephone)
            time.sleep(1)
            # self.driver.find_element(By.CLASS_NAME, self.getrole).click()
            # Select(self.driver.find_element(By.NAME, self.role)).select_by_visible_text(role)
            if gender < 4:
                self.gender = "//*[@id='gender']/label[{}]".format(gender)
                self.driver.find_element(By.XPATH, self.gender).click()
            time.sleep(1)

            self.driver.find_element(By.ID, self.save).click()
            time.sleep(2)

            if suc == '1':
                return self.flag
            elif suc == '2':
                self.flag = self.driver.find_element(By.XPATH, self.fall1).text
                return self.flag
            elif suc == '3':
                self.flag = self.driver.find_element(By.XPATH, self.fall2).text
                return self.flag
            elif suc == '4':
                self.flag = self.driver.find_element(By.XPATH, self.fall3).text
                return self.flag
            elif suc == '5':
                self.flag = self.driver.find_element(By.XPATH, self.fall4).text
                return self.flag
        except Exception as e:
            self.logs.error_log("失败原因: %s" % e)
        finally:
            self.driver.quit()

    def delete(self, target):
        try:
            self.driver.find_element(By.XPATH, self.depth1).click()
            self.driver.find_element(By.XPATH, self.depth2).click()
            time.sleep(2)

            table = self.driver.find_element(By.ID, self.table)
            table_rows = table.find_elements(By.TAG_NAME, 'tr')
            table_cols = table_rows[target].find_elements(By.TAG_NAME, 'td')
            table_cols[0].find_element(By.TAG_NAME, 'input').click()
            time.sleep(2)
            btelements = table.find_elements(By.TAG_NAME, 'button')
            btelements[3].click()

            self.driver.find_element(By.XPATH, self.deletconf).click()

            return self.deflag
        except Exception as e:
            self.logs.error_log("错误%s" % e)
