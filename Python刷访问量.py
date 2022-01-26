from bs4 import BeautifulSoup
import requests
import random
import time

def create_proxy_pool():
    # 从西拉免费ip代理网站获取代理IP列表
    r = requests.get('https://www.kuaidaili.com/free/', headers= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'})
    # 返回解析得到的的html
    soup = BeautifulSoup(r.content, 'lxml')
    # 获取所有ip，构成ips列表
    ips = soup.findAll('tr')
    # 初始化ip池空列表
    proxy_pool = []
    # 循环遍历ips列表
    for i in range(1, len(ips)):
        # ip_row是ips中的行
        ip_row = ips[i]
        # tds是每行中的属性值列表
        tds = ip_row.findAll("td")
        # 从一行中提取出proxy
        proxy = {'http':tds[0].get_text()}
        # 添加到代理池
        proxy_pool.append(proxy)
    return proxy_pool

# 代理客户端列表
user_agents = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"
]

# 创建请求头信息
def create_headers():
    headers = dict()
    headers["User-Agent"] = random.choice(user_agents)
    return headers

def startworking():

    page_list = ['https://blog.csdn.net/qq_45717425/article/details/122639288', 'https://blog.csdn.net/qq_45717425/article/details/122638358',
                 'https://blog.csdn.net/qq_45717425/article/details/122638191', 'https://blog.csdn.net/qq_45717425/article/details/122622663',
                 'https://blog.csdn.net/qq_45717425/article/details/122622520', 'https://blog.csdn.net/qq_45717425/article/details/122622459',
                 'https://blog.csdn.net/qq_45717425/article/details/122621085', 'https://blog.csdn.net/qq_45717425/article/details/122620464',
                 'https://blog.csdn.net/qq_45717425/article/details/122432586', 'https://download.csdn.net/download/qq_45717425/45358584',
                 'https://blog.csdn.net/qq_45717425/article/details/121170104', 'https://zhuanlan.zhihu.com/p/460159171']
    # 调用请求头
    # headers = create_headers()
    proxy_pool = create_proxy_pool()
    # print('请求头：%s' % headers)
    print('代理ip池：%s' % proxy_pool)
    # 循环构造并向服务器发送请求
    for i in range(1000):
        page1 = random.choice(page_list)
        print('正在进行第%s次访问...' % i)
        # 从ip池中随机选择一个代理ip
        proxy = random.choice(proxy_pool)
        print('当前代理IP: %s' % proxy)
        # 两次请求应间隔60s，否则会被认为是同一次访问
        sleep_time = random.randint(20,30)
        print('当前等待时间：%ds' % sleep_time)
        time.sleep(sleep_time)
        r = requests.get(url=page1, timeout=50, proxies=proxy, headers= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'})
        html = r.content
        soup = BeautifulSoup(html, "lxml")
        title =  soup.find('h1')
        # 爬取文章的标题及当前访问次数
        read_count = soup.find('span', attrs={'class': 'read-count'})
        #print('文章标题：%s' % title.get_text())
        # print('当前文章访问量：%s\n' % read_count.get_text())

if __name__ =='__main__':
    startworking()
