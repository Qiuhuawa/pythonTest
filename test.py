from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def main():
    chrome_option = Options()
    chrome_option.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome()
    driver.get("https://www.ptpress.com.cn/")

    driver.find_element(By.CSS_SELECTOR, "div > input").send_keys("1")
    driver.find_element(By.CSS_SELECTOR, "#header > div.container.clearfix > div > div.search > img").click()



    input()

    #加入断言
    assert driver.title == "selenium_百度搜索"  #断言页面跳转

    driver.quit()


if __name__ == '__main__':
    main()
