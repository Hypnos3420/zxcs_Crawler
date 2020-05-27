#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 " Author              :Hypnos3420
 " version             :v1.00 beta
 " Github              :https://github.com/Hypnos3420
 " Date                :2020-05-27 10:12:16
 " LastEditors         :Do not edit
 " LastEditTime        :2020-05-27 10:12:17
 " Description         :# NOTE 知轩藏书爬虫
"""


import re
import time

import requests


def getHTMLText(url):
    """
    获取HTMLText
    Attributes:
        url:网页地址
    Returns:
        requests结构体，包含HTML内容
    """
    try:
        kv = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0"
        }
        request = requests.get(url, headers=kv, timeout=30)
        request.raise_for_status()
        request.encoding = request.apparent_encoding
        print("爬取成功！\n"+request.text[: 1000])
    except Exception as e:
        return "产生异常：" + str(e)


# def findHTMLText(text):
#     soup = BeautifulSoup(text, "html.parser")
#     return soup.find_all(string=re.compile('知轩藏书'))


# 精校科幻页面
url = 'http://www.zxcs.me/sort/40'

if __name__ == "__main__":
    text = getHTMLText(url)
    # res = findHTMLText(text)
    # print(res)

print('asdfasdf')
