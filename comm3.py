from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def main():
    chrome_option = Options()
    chrome_option.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(options=chrome_option)
    driver.get("https://www.baidu.com/")

    bt1 = driver.find_element(By.ID, 's-usersetting-top')
    ActionChains(driver).move_to_element(bt1).perform()
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, '#s-user-setting-menu > div > a.setpref.first > span').click()
    time.sleep(2)
    driver.find_element(By.ID, 'nr_2').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '#se-setting-7 > a.prefpanelgo.setting-btn.c-btn.c-btn-primary').click()
    time.sleep(2)

    driver.switch_to.alert.accept()

    input()

    #加入断言
    assert driver.title == "selenium_百度搜索"  #断言页面跳转

    driver.quit()


if __name__ == '__main__':
    main()
