from selenium import webdriver
import time
from random import *

print("正在执行操作......")
# 给出所需的url和option参数
url_survey = ("https://www.wjx.cn/xx/xxxxxxx.aspx") # 根据需要填写url
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=option)
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
driver.get(url_survey)
time.sleep(2)

# 处理Q1
# 生成随机数，决定点哪个按钮
q1 = random()
if 0 <= q1 <= 0.5:
    # 通过属性定位元素
    # q1_1是Q1的第1个按钮
    driver.find_element_by_xpath("//a[@rel='q1_1']").click()
else:
    driver.find_element_by_xpath("//a[@rel='q1_2']").click()

# 处理Q2
# 生成随机数，决定点哪个按钮
q2 = random()
if 0 <= q2 <= 0.25:
    driver.find_element_by_xpath("//a[@rel='q2_1']").click()
elif 0.25 < q2 <= 0.50:
    driver.find_element_by_xpath("//a[@rel='q2_2']").click()
elif 0.50 < q2 <= 0.75:
    driver.find_element_by_xpath("//a[@rel='q2_3']").click()
else:
    driver.find_element_by_xpath("//a[@rel='q2_4']").click()

# 处理Q3
# 生成随机数，决定点哪个按钮
q3 = random()
if 0 <= q3 <= 0.25:
    driver.find_element_by_xpath("//a[@rel='q3_1']").click()
elif 0.25 < q3 <= 0.50:
    driver.find_element_by_xpath("//a[@rel='q3_2']").click()
elif 0.50 < q3 <= 0.75:
    driver.find_element_by_xpath("//a[@rel='q3_3']").click()
else:
    driver.find_element_by_xpath("//a[@rel='q3_4']").click()

# 处理Q4
# 生成随机数，决定点哪个按钮
q4 = random()
driver.find_element_by_xpath("//a[@rel='q4_1']").click()
driver.find_element_by_xpath("//a[@rel='q4_2']").click()
driver.find_element_by_xpath("//a[@rel='q4_3']").click()
driver.find_element_by_xpath("//a[@rel='q4_5']").click()
driver.find_element_by_xpath("//a[@rel='q4_7']").click()
if 0 <= q4 <= 0.15:
    driver.find_element_by_xpath("//a[@rel='q4_4']").click()
elif 0.15 < q4 <= 0.30:
    driver.find_element_by_xpath("//a[@rel='q4_6']").click()
elif 0.30 < q4 <= 0.45:
    driver.find_element_by_xpath("//a[@rel='q4_8']").click()
elif 0.45 < q4 <= 0.60:
    driver.find_element_by_xpath("//a[@rel='q4_9']").click()
elif 0.45 < q4 <= 0.60:
    driver.find_element_by_xpath("//a[@rel='q4_10']").click()
else:
    driver.find_element_by_xpath("//a[@rel='q4_11']").click()

# 处理Q5
# 生成随机数，决定点哪个按钮
q5 = random()
if 0 <= q5 <= 0.25:
    driver.find_element_by_xpath("//a[@rel='q5_1']").click()
    driver.find_element_by_xpath("//a[@rel='q5_2']").click()
    driver.find_element_by_xpath("//a[@rel='q5_3']").click()
elif 0.25 < q5 <= 0.50:
    driver.find_element_by_xpath("//a[@rel='q5_1']").click()
    driver.find_element_by_xpath("//a[@rel='q5_2']").click()
    driver.find_element_by_xpath("//a[@rel='q5_4']").click()
elif 0.50 < q5 <= 0.75:
    driver.find_element_by_xpath("//a[@rel='q5_2']").click()
    driver.find_element_by_xpath("//a[@rel='q5_3']").click()
    driver.find_element_by_xpath("//a[@rel='q5_4']").click()
else:
    driver.find_element_by_xpath("//a[@rel='q5_1']").click()
    driver.find_element_by_xpath("//a[@rel='q5_2']").click()
    driver.find_element_by_xpath("//a[@rel='q5_3']").click()
    driver.find_element_by_xpath("//a[@rel='q5_4']").click()

# 处理Q6
# 生成随机数，决定点哪个按钮
q6 = random()
if 0 <= q6 <= 0.50:
    driver.find_element_by_xpath("//a[@rel='q6_2']").click()
elif 0.50 < q6 <= 0.60:
    driver.find_element_by_xpath("//a[@rel='q6_1']").click()
else:
    driver.find_element_by_xpath("//a[@rel='q6_3']").click()

# 处理Q7
# 生成随机数，决定点哪个按钮
q7 = random()
if 0 <= q7 <= 0.95:
    driver.find_element_by_xpath("//a[@rel='q7_1']").click()
elif 0.95 < q7 <= 0.98:
    driver.find_element_by_xpath("//a[@rel='q7_2']").click()
else:
    driver.find_element_by_xpath("//a[@rel='q7_3']").click()

# 处理Q8
# 生成随机数，决定点哪个按钮
q8 = random()
if 0 <= q8 <= 0.20:
    driver.find_element_by_xpath("//a[@rel='q8_1']").click()
    driver.find_element_by_xpath("//a[@rel='q8_2']").click()
    driver.find_element_by_xpath("//a[@rel='q8_3']").click()
    driver.find_element_by_xpath("//a[@rel='q8_4']").click()
elif 0.20 < q8 <= 0.40:
    driver.find_element_by_xpath("//a[@rel='q8_1']").click()
    driver.find_element_by_xpath("//a[@rel='q8_2']").click()
    driver.find_element_by_xpath("//a[@rel='q8_3']").click()
    driver.find_element_by_xpath("//a[@rel='q8_5']").click()
elif 0.20 < q8 <= 0.40:
    driver.find_element_by_xpath("//a[@rel='q8_1']").click()
    driver.find_element_by_xpath("//a[@rel='q8_2']").click()
    driver.find_element_by_xpath("//a[@rel='q8_4']").click()
    driver.find_element_by_xpath("//a[@rel='q8_5']").click()
elif 0.20 < q8 <= 0.40:
    driver.find_element_by_xpath("//a[@rel='q8_1']").click()
    driver.find_element_by_xpath("//a[@rel='q8_3']").click()
    driver.find_element_by_xpath("//a[@rel='q8_4']").click()
    driver.find_element_by_xpath("//a[@rel='q8_5']").click()
else:
    driver.find_element_by_xpath("//a[@rel='q8_1']").click()
    driver.find_element_by_xpath("//a[@rel='q8_2']").click()
    driver.find_element_by_xpath("//a[@rel='q8_3']").click()
    driver.find_element_by_xpath("//a[@rel='q8_4']").click()
    driver.find_element_by_xpath("//a[@rel='q8_5']").click()

# 处理Q9
# 生成随机数，决定点哪个按钮
q9 = random()
driver.find_element_by_xpath("//a[@rel='q9_1']").click()
driver.find_element_by_xpath("//a[@rel='q9_3']").click()
driver.find_element_by_xpath("//a[@rel='q9_4']").click()
driver.find_element_by_xpath("//a[@rel='q9_5']").click()
driver.find_element_by_xpath("//a[@rel='q9_7']").click()
if 0 <= q9 <= 0.33:
    driver.find_element_by_xpath("//a[@rel='q9_2']").click()
elif 0.33 < q9 <= 0.66:
    driver.find_element_by_xpath("//a[@rel='q9_6']").click()
else:
    driver.find_element_by_xpath("//a[@rel='q9_8']").click()

# 处理Q10
# 生成随机数，决定点哪个按钮
q10 = random()
driver.find_element_by_xpath("//a[@rel='q10_2']").click()
driver.find_element_by_xpath("//a[@rel='q10_4']").click()
if 0 <= q10 <= 0.50:
    driver.find_element_by_xpath("//a[@rel='q10_3']").click()
else:
    driver.find_element_by_xpath("//a[@rel='q10_1']").click()

# 处理Q11
# 生成随机数，决定点哪个按钮
q11 = random()
driver.find_element_by_xpath("//a[@rel='q11_1']").click()
driver.find_element_by_xpath("//a[@rel='q11_2']").click()
driver.find_element_by_xpath("//a[@rel='q11_3']").click()
if 0 <= q11 <= 0.25:
    driver.find_element_by_xpath("//a[@rel='q11_4']").click()
elif 0.25 < q9 <= 0.50:
    driver.find_element_by_xpath("//a[@rel='q11_5']").click()
elif 0.50 < q9 <= 0.75:
    driver.find_element_by_xpath("//a[@rel='q11_6']").click()
else:
    driver.find_element_by_xpath("//a[@rel='q11_7']").click()

# 处理Q12
# 生成随机数，决定点哪个按钮
q12 = random()
if 0 <= q12 <= 0.85:
    driver.find_element_by_xpath("//a[@rel='q12_1']").click()
elif 0.85 < q12 <= 0.95:
    driver.find_element_by_xpath("//a[@rel='q12_2']").click()
else:
    driver.find_element_by_xpath("//a[@rel='q12_3']").click()

# 处理Q13
driver.find_element_by_xpath("//a[@rel='q13_1']").click()
driver.find_element_by_xpath("//a[@rel='q13_2']").click()
driver.find_element_by_xpath("//a[@rel='q13_3']").click()

# 模拟点击提交按钮
driver.find_element_by_xpath("//input[@value='提交']").click()
time.sleep(0.5)

# 模拟点击智能验证按钮
# 先点确认
driver.find_element_by_xpath("//button[text()='确认']").click()
# 再点智能验证提示框，进行智能验证
driver.find_element_by_xpath("//div[@id='captcha']").click()