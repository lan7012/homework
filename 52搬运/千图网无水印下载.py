'''import re
import urllib.request
import time
# proxy = urllib.request.ProxyHandler({"http" :"183.172.192.248:1080"})
# opener = urllib.request.build_opener(proxy ,urllib.request.HTTPHandler)
# urllib.request.install_opener(opener)
count = 0
try:
    for c in range(0,10):
        new_url = "http://bbs.zol.com.cn/dcbbs/d16_good_p" + str(c) + ".html#c"
        data_new = urllib.request.urlopen(new_url).read().decode("utf-8","ignore")
        tj_new = 'data-url="/dcbbs/(.*?).html">'
        p1 = re.compile(tj_new).findall(str(data_new))

        for sen in range(len(p1)):
            url = "http://bbs.zol.com.cn/dcbbs/" + str(p1[sen]) + ".html"
            data = urllib.request.urlopen(url).read().decode("GBK","ignore")
            tj = 'data-original="https://bbs-fd.zol-img.com.cn/t_s(.*?).jpg'
            p = re.compile(tj).findall(data)
            for i in range(len(p)):
                url = "https://bbs-fd.zol-img.com.cn/t_s" + str(p[i]) + ".jpg"
                file = "F:/bing/摄影论坛/" + str(p[i][-8:-1]) + ".jpg"
                count +=1
                if count%5 ==0:
                    time.sleep(0.65)
                print("正在保存第%s张图片" % count)
                urllib.request.urlretrieve(url,filename=file)
except urllib.error.URLError as e:
    if hasattr(e, 'code'):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)'''

import re
import urllib.request
url_baba = "https://www.58pic.com/newpic/32681878.html"
data = urllib.request.urlopen(url_baba).read().decode('gbk','ignore')
tj = 'content="//preview.(.*?)!w1024_water'
mp4_tj = 'data-src="//pic.qiantucdn.com/58pic/(.*?)"'
title_tj = '<span class="pic-title fl">(.*?)</span>'
p = re.compile(tj).findall(str(data))
tit = re.compile(title_tj).findall(str(data))
mp4_p = re.compile(mp4_tj).findall(str(data))
h_z = p[0][-4:]
for i in range(len(p)):
    if mp4_p ==[]:
        pass
    else:
        print("发现视频，开始下载")
        mp4_hz = mp4_p[0][-4:]
        url = "http://pic.qiantucdn.com/58pic/" + str(mp4_p[0])
        file = "F:/bing/千图网无损/" + str(tit[0]) + str(mp4_hz)
        urllib.request.urlretrieve(url, filename=file)
        print("下载成功:" + str(tit[0]))
        continue
    url = "http://pic." + str(p)
    file = "F:/bing/千图网无损/" + str(tit[0]) +str(h_z)
    urllib.request.urlretrieve(url,filename=file)
    print("下载成功:" +str(tit[0]))