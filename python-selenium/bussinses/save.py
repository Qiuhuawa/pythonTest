import pandas as pd
import math
from selenium import webdriver
import time

data = []
def save(tr_list):
    # for i in range(numbers):
    for tr in tr_list:
        td_list = tr.find_elements_by_tag_name('td')  # 定位表格每个单元格
        lst = []  # 建立空列表存储每行信息
        for td in td_list:
            # lst.append("report-BinaryScan")  # 添加版本信息
            lst.append(td.text)  # 添加每个单元格的文本信息
            href = td_list[4].find_element_by_tag_name('a').get_attribute("href")  # 获当前行第5个td单元格的超链接
        print(u"第n行第n列的text:", href)
        lst.append(href)  # print(u"第一行第二列的text:", href)  # 添加文件链接
        data.append(lst)  # 添加每行信息

    # 点击下一页逻辑判断
    # 如果table只有1页，不作处理，直接退出循环
    # 如果table只有2页，点击下一页处理条件（total_pages == 3 and i == 1）
    # 如果table2页以上，点击下一页处理条件（total_pages > 3 and i < (total_pages - 1)）

    df = pd.DataFrame(data,
        columns=['选择', '策略', '审核', '版本组', '匹配数', '3', '4', '5', '6', '7', '8', '9', '10',
            '来源链接'])
    df.to_csv('save.csv', encoding='utf_8_sig')