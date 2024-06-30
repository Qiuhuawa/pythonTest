from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def main():
    chrome_option = Options()
    #chrome_option.add_argument('--disable-dev-shm-usage')
    chrome_option.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(options=chrome_option)
    driver.get("https://www.acwing.com")

    time.sleep(5)
    driver.find_element(By.XPATH, "/html/body/div[2]/nav/div/div[2]/ul[2]/li[3]/a").click()
    time.sleep(10)

    driver.find_element(By.ID, "login_username").send_keys("1010565096@qq.com")
    driver.find_element(By.ID, "login_password").send_keys("Cheng031120")
    driver.find_element(By.ID, "login_remember_me").click()
    time.sleep(2)

    driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/form[1]/div[2]/div[1]/button").click()

    input()

    #加入断言
    assert driver.title == "selenium_acwing"  #断言页面跳转

    driver.quit()


if __name__ == '__main__':
    main()
