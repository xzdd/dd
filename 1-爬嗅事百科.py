# coding:utf-8
from bs4 import BeautifulSoup
import requests
r = requests.get("https://www.qiushibaike.com/")
qiubai = r.content
soup = BeautifulSoup(qiubai, "html.parser")
duanzi = soup.find_all(class_="content")
for i in duanzi:
# tag 的 .contents 属性可以将 tag 的子节点以列表的方式输出
    duan = i.span.contents[0] # 取第一个
    print (duan)
