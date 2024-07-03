import ddt
import os
import unittest
from selenium import webdriver

from bussinses.amazingday import Login_tes
from util import log
from util.gettestdata import getmessage_test
from selenium.webdriver.chrome.options import Options

path = os.getcwd()
case_path = path + '\\data\\case.xlsx'
case_data = getmessage_test(case_path, 0)


@ddt.ddt
class Testlogin(unittest.TestCase):
    def setUp(self):
        chrome_option = Options()
        self.logs = log.log_message()
        chrome_option.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.driver = webdriver.Chrome(options=chrome_option)
        self.login_fun = Login_tes(self.driver)

    @ddt.data(*case_data)
    def test_login1(self, login_data):
        self.name = login_data['username']
        self.pwd = login_data['pwd']
        self.suc = login_data['suc']
        self.assert_value = login_data['assert']
        self.logs.info_log(
            'input data:name:%s,pwd:%s,assert:%s' % (self.name, self.pwd, self.assert_value))
        self.re_data = self.login_fun.login(self.suc, self.name, self.pwd)
        self.assertEqual(self.re_data, self.assert_value)

    def tearDown(self):
        self.driver.quit()
