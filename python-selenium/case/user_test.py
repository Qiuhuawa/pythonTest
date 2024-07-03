import time

import ddt
import os
import unittest
from selenium import webdriver

from bussinses.amazingday import User_tes
from bussinses.login import login
from util import log
from util.gettestdata import getmessage_test
from selenium.webdriver.chrome.options import Options

path = os.getcwd()
case_path = path + '\\data\\case.xlsx'
case_data = getmessage_test(case_path, 1)
dele_data = getmessage_test(case_path, 2)


@ddt.ddt
class Testuser(unittest.TestCase):
    def setUp(self):
        chrome_option = Options()
        self.logs = log.log_message()
        chrome_option.add_experimental_option("excludeSwitches", ['enable-automation'])
        chrome_option.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=chrome_option)
        self.login = login(self.driver)
        self.login.login("admin", "30473860")
        self.user_fun = User_tes(self.driver)

    @ddt.data(*case_data)
    def test_user1(self, user_data):
        self.useraccount = user_data['account']
        self.username = user_data['name']
        self.iduser = user_data['userid']
        self.useremail = user_data['email']
        self.usertelephone = user_data['telephone']
        self.user_suc = user_data['suc']
        self.usergender = user_data['gender']
        self.assert_value = user_data['assert']
        self.logs.info_log(
            'insert data: account:%s, name:%s, id:%s, email:%s, telephone:%s, gender:%i,suc:%s,  assert:%s' % (
                self.useraccount, self.username, self.iduser, self.useremail, self.usertelephone,
                self.usergender, self.user_suc, self.assert_value)
        )
        self.re_data = self.user_fun.add(
            self.user_suc, self.useraccount, self.username, self.iduser, self.useremail, self.usertelephone,
            self.usergender
        )
        self.assertEqual(self.re_data, self.assert_value)

    @ddt.data(*dele_data)
    def test_user2(self, user_data):
        self.targetuser = user_data['target']
        self.re_data = self.user_fun.delete(self.targetuser)
        self.assert_value2 = user_data['assert']
        self.assertEqual(self.re_data, self.assert_value2)

    def tearDown(self):
        self.driver.quit()