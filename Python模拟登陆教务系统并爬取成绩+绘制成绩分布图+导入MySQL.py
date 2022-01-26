# coding=utf-8
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import matplotlib.pyplot as plt
import time
import pymysql

# 给出所需的url
url_login_page = ("https://ids.xidian.edu.cn/authserver/login?service=https%3A%2F%2Fehall.xidian.edu.cn%3A443%2Flogin%3Fservice%3Dhttps%3A%2F%2Fehall.xidian.edu.cn%2Fnew%2Findex.html")
url_cjcx=("http://ehall.xidian.edu.cn/jwapp/sys/cjcx/*default/index.do?amp_sec_version_=1&gid_=WkxQdVVYSXQ4eGlmSXNuV28wWlRobnZ1WmtlaWRsUmZaU1pwSWYrYnJpZEZSZGoxU3JzQ0hkL0NicE93UmRsSnNtY01TMDZmcTZFZytHTFhQOXdjY2c9PQ&EMAP_LANG=zh&THEME=cherry#/cjcx")

# 启动Chorme驱动，开始模拟（不能用静默模式启动）
option = webdriver.ChromeOptions()
# 不加载图片，提高访问速度
option.add_argument('blink-settings=imagesEnabled=false')
driver = webdriver.Chrome(chrome_options=option)
driver.maximize_window()
print("正在访问......")
driver.get(url_login_page)

# 自动输入账号密码
driver.find_element_by_id("username").send_keys("19030100075")
driver.find_element_by_id("password").send_keys("tzchen_20010102tzc")

# 找到并点击登录按钮，实现登录
login_button = driver.find_element_by_id("login_submit")
actions = ActionChains(driver)
actions.key_down(Keys.CONTROL).click(login_button).key_up(Keys.CONTROL).perform()

# 打开新的地址
driver.switch_to.window(driver.window_handles[-1])
driver.get(url_cjcx)

# 等待页面加载完毕
time.sleep(10)

# 找到每页显示数目选择框并点击"50"
driver.find_element_by_class_name("bh-pull-right.jqx-widget.jqx-dropdownlist-state-normal.jqx-rc-all.jqx-fill-state-normal").click()
time.sleep(0.5)
driver.find_element_by_xpath("//span[text()='50']").click()

# 等待页面加载完毕
time.sleep(1)

# 准备爬取成绩查询页面的信息
data = driver.page_source
soup = BeautifulSoup(data, 'lxml')
trs = soup.find_all("tr")
total_container = []
for tr in trs:
    row_container = []
    for span in tr:
        row_container.append(span.string)
    total_container.append(row_container)

# 初始化score subjects列表
score = []
subjects = []

# 输出最近两学期成绩数据
print("近两学期所有科目成绩如下：")
subject_num = int(len(total_container)/2)
for i in range(1,subject_num+1):
    print(total_container[i-1][1], total_container[i-1][2], total_container[i-1][6], total_container[i-1][9], total_container[i-1][11])
    subjects.append(total_container[i-1][2])
    score.append(total_container[i-1][6])
print("\n原始成绩：",score,"\n")

# 规范化成绩
for i in range(1,subject_num+1):
    if score[i-1] == '优秀' or score[i-1] =='621':
        score[i-1] = 95
    elif score[i-1] == '良好':
        score[i-1] = 85
    elif score[i-1] == '通过':
        score[i-1] = 75
    elif score[i-1] == None:
        score[i-1] = 98
    else:
        score[i-1] = int(score[i-1])

print("科目：",subjects,"\n")
print("规范化后的成绩：",score)

# # 绘图
# print("\n正在绘制成绩分布折线图...")
# x = range(subject_num)
# # plt.xticks(x,subjects)  # 可以设置坐标字
# plt.plot(x, score)
# plt.xlabel("Subject(The xth)") #X轴标签
# plt.ylabel("Score") #Y轴标签
# plt.title('Score Distribution Chart')
# plt.show()

# 写入MySQL
print("\n正在连接MySQL服务\n...")
# 创建与测试数据库的连接
conn = pymysql.connect(host='localhost',user="root",password="tzchen_20010102",database="score_db")
# 输出创建的连接对象的信息
print("连接成功!\n连接对象的基本信息如下：")
print (conn)
print (type(conn))
cursor = conn.cursor()
print("开始向数据表插入爬取的内容...")
sql1 = ("INSERT INTO score_table_test(学期,课程名,总成绩,课程性质,学分) VALUES(%s,%s,%s,%s,%s)")
for i in range(1,subject_num+1):
    # param中是实际的表格数据
    param = (total_container[i-1][1], total_container[i-1][2], total_container[i-1][6], total_container[i-1][9], total_container[i-1][11])
    cursor.execute(sql1, param)
    conn.commit()
print("插入成功!")
# 清空表格内容
print("正在清空当前表格内容...")
sql2 = ("truncate table score_table_test")
cursor.execute(sql2)
conn.commit()
print("删除成功！")
# 关闭指针对象和连接对象
print("准备断开数据库连接....")
cursor.close()
conn.close()
print("已成功断开连接！")