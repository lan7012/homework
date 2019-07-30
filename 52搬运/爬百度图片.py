import requests
import re
import time
from urllib import parse

name = "崩坏3"  # 搜索的关键字
name_url = {'word': name}
name_word = parse.urlencode(name_url)  # 编码转换
y = 0  # 页数计数，从0开始依次加60，百度的3页为这里的一页
i = 1  # 文件计数
# 模仿浏览器
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
while True:
    url = 'http://image.baidu.com/search/index?tn=baiduimage&ipn=utf-8&sid=&' + name_word + '&pn=' + str(y)
    print('第' + str(int(y / 60)) + '页')
    data = requests.get(url, headers=headers).text  # 获取页面数据
    url_img = re.findall('"objURL":".*?",', data)
    # 遍历图片url
    for s in url_img:
        img_url = s.lstrip('"objURL":"').rstrip('",')
        img_fi = s.lstrip('"objURL":"').rstrip('",')[-4:]  # 获取拓展名
        img_name = img_url.split('/')[-1].rstrip(img_fi)
        img_le = img_fi[-4]
        if img_le == ".":  # 筛选数据
            try:  # 异常处理
                img = requests.get(img_url, headers=headers).content
                # 保存图片
                with open('img/' + img_name + img_fi, 'wb') as f:
                    f.write(img)
                    print("图片" + img_name + ' 第' + str(i) + '张' + " 地址：" + img_url)
                    time.sleep(1)
                    i = i + 1
            except:
                print('访问链接出错')
    y = y + 60