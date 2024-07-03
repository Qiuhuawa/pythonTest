from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def main():
    chrome_option = Options()
    #chrome_option.add_argument('--disable-dev-shm-usage')
    chrome_option.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(options=chrome_option)
    driver.get("https://www.xxx")

    time.sleep(5)
    driver.find_element(By.XPATH, "xxxxxxxxx").click() #点击登录
    time.sleep(10)

    driver.find_element(By.ID, "login_username").send_keys("xxxxx@xxx.com")
    driver.find_element(By.ID, "login_password").send_keys("xxxxxxxx")
    driver.find_element(By.ID, "login_remember_me").click()
    time.sleep(2)

    driver.find_element(By.XPATH,"xxxxxx").click() #登录确认按钮

    input()

    #加入断言
    assert driver.title == "selenium_acwing"  #断言页面跳转

    driver.quit()


if __name__ == '__main__':
    main()
