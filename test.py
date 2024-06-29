from selenium import webdriver

def main():
    # 未配置 # chrome_driver 存放位置
    driver = webdriver.Chrome()  # 调用Chrome()类

    driver.get("https://www.baidu.com")  # 访问百度首页

    driver.find_element_by_id("kw").send_keys("Selenium")  # 输入"Selenium"
    driver.find_element_by_id("su").click()  # 提交查询

    driver.quit()  # 关闭浏览器


if __name__ == '__main__':
    main()