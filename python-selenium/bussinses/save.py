import pandas as pd
import math
from selenium import webdriver
import time

data = []
def save(tr_list):
    # for i in range(numbers):
    for tr in tr_list:
        td_list = tr.find_elements_by_tag_name('td')  # ��λ���ÿ����Ԫ��
        lst = []  # �������б�洢ÿ����Ϣ
        for td in td_list:
            # lst.append("report-BinaryScan")  # ��Ӱ汾��Ϣ
            lst.append(td.text)  # ���ÿ����Ԫ����ı���Ϣ
            href = td_list[4].find_element_by_tag_name('a').get_attribute("href")  # ��ǰ�е�5��td��Ԫ��ĳ�����
        print(u"��n�е�n�е�text:", href)
        lst.append(href)  # print(u"��һ�еڶ��е�text:", href)  # ����ļ�����
        data.append(lst)  # ���ÿ����Ϣ

    # �����һҳ�߼��ж�
    # ���tableֻ��1ҳ����������ֱ���˳�ѭ��
    # ���tableֻ��2ҳ�������һҳ����������total_pages == 3 and i == 1��
    # ���table2ҳ���ϣ������һҳ����������total_pages > 3 and i < (total_pages - 1)��

    df = pd.DataFrame(data,
        columns=['ѡ��', '����', '���', '�汾��', 'ƥ����', '3', '4', '5', '6', '7', '8', '9', '10',
            '��Դ����'])
    df.to_csv('save.csv', encoding='utf_8_sig')