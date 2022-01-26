# coding = utf-8
from bs4 import BeautifulSoup
import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
url = "https://jbk.39.net/mxyy/jbzs/"
r = requests.get(url, headers = headers)
html = r.content.decode('utf-8', 'ignore')
my_page = BeautifulSoup(html, 'lxml')

for tag in my_page.find_all('div', class_='disease'):   
    disease = tag.find('h1').get_text()
    disease_name = disease

for tag in my_page.find_all('p', class_='introduction'):
    introduction = tag.get_text()
    disease_introduction = introduction

for tag in my_page.find_all('div', class_='list_left'):
    sub_tag = tag.find('ul',class_="disease_basic") 
    my_span = sub_tag.findAll('span')
    #my_span is a list
    is_yibao = my_span[1].text    #是否医保
    othername = my_span[3].text   #别名
    fbbw = my_span[5].text        #发病部位
    is_infect = my_span[7].text   #传染性
    dfrq = my_span[9].text        #多发人群
    my_a = sub_tag.findAll('a')
    xgzz = my_a[2].text+' '+my_a[3].text+' '+my_a[4].text  #相关症状
    #ps: .contents[0] or .get_text() is also accepted

# Some tests:
# print(html)
# print(my_page)
# print(sub_tag)
# print(xgzz)
# print(my_span)
# print(my_span[1])

import pymysql
print("*************************************\n以下进行连接数据库及数据写入操作：\n")
print('正在连接MySQL服务\n......')
#创建与测试数据库的连接
conn = pymysql.connect(host='localhost',user="root",password="xxxxxxxxxx",database="testdb")
#输出创建的连接对象的信息
print('连接成功!\n连接对象的基本信息如下：')
print (conn)
print (type(conn))
print("\n")
cursor = conn.cursor()
print('开始向数据表插入爬取内容\n......')
sql1 = ("INSERT INTO test_table(id,disease_name,is_yibao,other_name,is_infect,fbbw) VALUES(%s,%s,%s,%s,%s,%s)")
param = ("1",disease_name,is_yibao,othername,is_infect,fbbw)
cursor.execute(sql1, param)
conn.commit()
print('插入成功!\n')
print("\n本次实验操作已完成，准备断开数据库连接\n......")
#关闭指针对象和连接对象
cursor.close()
conn.close()
print("已成功断开连接！")
print("实验结束。")
