from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def main():
    chrome_option = Options()
    #chrome_option.add_argument('--disable-dev-shm-usage')
    chrome_option.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(options=chrome_option)
    driver.get("https://www.baidu.com")

    time.sleep(2)
    driver.find_element(By.ID, "s-top-loginbtn").click()
    time.sleep(2)

    driver.find_element(By.ID, "TANGRAM__PSP_11__regLink").click()
    time.sleep(2)

    switch_window = driver.current_window_handle
    window_handles = driver.window_handles
    for h in window_handles:
        if h != switch_window:
            driver.switch_to.window(h)

    time.sleep(2)
    driver.find_element(By.ID, "TANGRAM__PSP_4__userName").send_keys("Chexxxxx")
    driver.find_element(By.ID, "TANGRAM__PSP_4__phone").send_keys("xxxxxx")
    driver.find_element(By.ID,"TANGRAM__PSP_4__password").send_keys("C11111111")
    # driver.find_element(By.ID,"TANGRAM__PSP_4__verifyCodeSend").click()
    time.sleep(3)
    driver.find_element(By.ID,"TANGRAM__PSP_4__verifyCode").send_keys("BC1234")


    # print(driver.find_element(By.CLASS_NAME, "pass-confirmContent-msg").text)
    if "该手机号已注册" in driver.find_element(By.CLASS_NAME, "pass-confirmContent-msg").text:
        driver.find_element(By.id, "TANGRAM__PSP_31__confirm_cancel").click()

    time.sleep(2)
    driver.find_element(By.ID,"TANGRAM__PSP_4__isAgree").click()
    driver.find_element(By.ID,"TANGRAM__PSP_4__submit").click()

    input()

    #加入断言
    assert driver.title == "selenium_baiduRegister"  #断言页面跳转

    driver.quit()


if __name__ == '__main__':
    main()
