import re
import ssl
import urllib.error
import urllib.request
headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
#ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://v.qq.com/x/cover/2lpgitasa9dvwb7.html'
mach = urllib.request.urlopen(url).read().decode("utf-8","ignoer")
sy_sj = '"comment_id":"(.*?)"'
pth = re.compile(sy_sj).findall(mach)[0]#获取评论第一页的号码
count =1
next_page = []
while True:
    if next_page !=[]:
        calls_url = 'https://video.coral.qq.com/varticle/' + str(pth) + '/comment/v2?callback=_varticle/' + str(pth) + '/commentv2&orinum=10&oriorder=o&pageflag=1&cursor=' + str(next_page[0])

        mach_data = urllib.request.urlopen(calls_url).read().decode("utf-8","ignore")

        id_title = '"content":"(.*?)"'
        com = '"last":"(.*?)"'
        data = re.compile(id_title).findall(mach_data)  # 过滤出评论
        next_page = re.compile(com).findall(mach_data)
        for i in range(len(data)):
            print("这是第"  + str(count) + "条评论")
            print(data[i])
            count +=1
    else:
        calls_url = 'https://video.coral.qq.com/varticle/' + str(pth) + '/comment/v2?callback=_varticle/' + str(pth) + '/commentv2&orinum=10&oriorder=o&pageflag=1&cursor='
        mach_data = urllib.request.urlopen(calls_url).read().decode("utf-8", "ignoer")
        com = '"last":"(.*?)"'
        next_page = re.compile(com).findall(mach_data)
        id_title = '"content":"(.*?)"'
        data = re.compile(id_title).findall(mach_data)  # 过滤出评论
        for i in range(len(data)):
            print("这是第" + str(count) + "条评论")
            print(data[i])
            count +=1
    if count ==101:
        break

