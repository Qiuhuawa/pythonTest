from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def main():
    chrome_option = Options()
    chrome_option.add_experimental_option("excludeSwitches", ['enable-automation'])

    driver = webdriver.Chrome(options=chrome_option)
    driver.get("https://www.baidu.com")

    # name定位
    # driver.find_element(By.NAME, "wd").send_keys("violet")
    # driver.find_element(By.ID, "su").click()

    # 通过tag定位输入框
    # driver.find_element(By.TAG_NAME, "input")

    # 通过class定位百度输入框与百度一下按钮
    # driver.find_element(By.CLASS_NAME, "s_ipt").send_keys("romantic")
    # time.sleep(2)
    # driver.find_element(By.CLASS_NAME, "s_btn").click()

    # 通过页面上“hao123”文本进行定位
    # driver.find_element(By.LINK_TEXT, "hao123").click()

    # 通过页面上“000001号”文本进行模糊匹配定位
    # time.sleep(2)
    # driver.find_element(By.PARTIAL_LINK_TEXT, "000001").click()

    # 绝对路径法
    # driver.find_element(By.XPATH, "/html/body/div/div/div[5]/div/div/form/span/input").send_keys("web 自动化测试")

    # //input，表示当前页面的input标签，[@id='kw']表示这个元素id值为kw
    # driver.find_element(By.XPATH, "//input[@id='kw']").send_keys("web 自动化测试")

    # //*,可以代替任何标签
    # driver.find_element(By.XPATH, "//*[@id='su']").click()

    # // 可以使用任何'唯一标识'的元素进行定位
    # driver.find_element(By.XPATH, "//*[@name='wd']").send_keys("web 自动化测试")
    # driver.find_element(By.XPATH, "//*[@type='submit']").click()

    # 可以先定位到父元素，然后使用/input,可以定位到其子类的input
    # time.sleep(2)
    # driver.find_element(By.ID, "kw").send_keys("web 自动化测试")
    # driver.find_element(By.XPATH, "//input[@id='kw' and @name='wd']").send_keys("firefly")
    # time.sleep(2)
    # driver.find_element(By.XPATH, "//form[contains(@id,'form')]/span[2]").find_element(By.TAG_NAME,"input").click()
    # driver.find_element(By.XPATH, "//span[contains(@class,'s_btn_wr')]/input").click()

    # 逻辑运算符，and 表示必须都满足
    # driver.find_element(By.ID, "kw").send_keys("selenium")
    # driver.find_element(By.XPATH, "//input[@id='su' and @class='bg s_btn']").click()

    # contains 方法匹配一个属性中包含的字符串
    # driver.find_element(By.XPATH, "//span[contains(@class,'s_ipt_wr')]/input").send_keys("selenium")
    # driver.find_element(By.ID, "su").click()

    # text()方法用于匹配显示文本的内容
    # driver.find_element(By.XPATH, "//a[text()='hao123']").click()

    # 通过 class 定位：使用点号（.）开头来定位 CSS 中的元素
    # driver.find_element(By.CSS_SELECTOR, ".s_ipt").send_keys("学习自动化测试")
    # driver.find_element(By.CSS_SELECTOR, ".s_btn").click()

    # 通过 id 定位：使用井号（#），通过 id 来定位元素
    # driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("学习自动化测试")
    # driver.find_element(By.CSS_SELECTOR, "#su").click()

    # CSS选择器中使用标签定位无需任何其他符号
    # driver.find_element(By.XPATH, "//form[@id='form']/span[2]").find_element(By.CSS_SELECTOR, "input").click()

    # 通过标签层级关系定位：根据父元素 span 定位到子元素 input
    # driver.find_element(By.CSS_SELECTOR, "span > input").send_keys("1")
    # 注：其实这句话用于查找该页面上第一个input，也就是输入框，若为“div > input”，则查询页面上每一个input

    # 通过属性定位：在CCS中，可以使用任何属性进行定位，只要这个属性可以唯一标识这个元素
    # driver.find_element(By.CSS_SELECTOR, '#kw').send_keys("I think, therefore I am")
    # driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    # 组合定位：在无法确定元素唯一性时，可以使用组合定位，加大定位元素的唯一性
    # driver.find_element(By.CSS_SELECTOR, 'span > input.s_ipt').send_keys("Viva La Vida")
    # driver.find_element(By.CSS_SELECTOR, 'span > [type="submit"]').click()

    # 直接锁定一组元素 # 循环遍历打印出元素组的文本内容
    # 需要注意find_elements(),要与find_element()区分开来
    # elements = driver.find_elements(By.CSS_SELECTOR, "#s-top-left > a")
    #
    # for element in elements:
    #     print(element.text)


    input()

    # 加入断言
    assert driver.title == "selenium_test"  # 断言页面跳转

    driver.quit()

if __name__ == '__main__':
    main()

