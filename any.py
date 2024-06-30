from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
#

driver_path = r"D:\Anaconda3\envs\paddle\Scripts\chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://www.taobao.com/")
computer_element = driver.find_element(By.CLASS_NAME,"cate-content-href")
#time.sleep(3)
ActionChains(driver).move_to_element(computer_element).perform()

hover_element = driver.find_element(By.CSS_SELECTOR,"body > div.screen-outer.clearfix > div.tbh-service.J_Module > div > ul > li.J_Cat.a-all.cate.show-sec-cate > div > div > div > div:nth-child(1) > a > div.sec-cate-txt-title")
hover_element.click()
time.sleep(3)

driver.quit()
