#!/usr/bin/python3

from sys import argv
from bs4 import BeautifulSoup
import requests, re

if len(argv) <=1:
    print("non-word")

word = ""
for index in range(len(argv)):
    if index == 0:
        continue
    word += argv[index] + " "

print('查询:', word)
print('...')

url = "http://www.iciba.com/" + word
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html5lib')

result = []
# 得到解释列表
for ul in soup.find_all('ul', class_="base-list switch_part"):
    for li in ul.find_all('li', class_="clearfix"):
        temp = {}
        temp['type'] = li.span.text.strip()
        spans = []
        for span in li.p:
            ret = span.string.strip().replace("\n", "")
            if len(ret) > 0:
                spans.append(ret)
        temp['result'] = spans
        result.append(temp)

if len(result) > 0:
    for ret in result:
        print('词性：',ret['type'])
        print(ret['result'])
else:
    print('没有结果')
