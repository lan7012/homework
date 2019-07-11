# coding:utf-8
#支持cookie登录和账号密码登陆（位置代码中自己找，print("* 模拟登陆... *")上面）；还加了换ip代{过}{滤}理的，不过好像没什么用。
#登录多了的话，豆瓣会要求验证码，所以也加了验证码识别，用的百度文字识别api，注册后加上access_token 就行；不想注册的话，我的可以借给大家~
#具体回复的评论url，可以用F12看一下，然后改到print("* 开始刷留言...* ")下面的urls里。
#if ("时光" in html_cookie.text):这里，把“时光”改成自己的昵称。
#去年的代码了，有点忘，大家试试吧、

import requests
import time
import sys, os
import random
from bs4 import BeautifulSoup
import re
from PIL import Image
import urllib.request, urllib.parse, urllib3, base64
import requests.adapters


def main():
    start_flag = False
    vcode_flag = False
    proxies = {'https': '134.249.165.49:53281'}
    Reload = 0
    while 1:
        if (Reload > 5):
            return
        img_code = ''
        img_id = ''
        ck = ''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        }
        if (start_flag == False):
            url_login = "https://accounts.douban.com/login"
            # requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
            sess = requests.session()
            sess.keep_alive = False  # 关闭多余连接
            # sess.proxies = proxies
            while 1:
                print("* 获取验证码... *")
                url_img = sess.get(url_login, headers=headers)
                if (url_img.status_code == 403):
                    print("* 登录次数过多，1小时后重试 *")
                    time.sleep(60 * 60)
                    continue
                soup = BeautifulSoup(url_img.text, 'lxml')
                try:
                    img = soup.find("img", id="captcha_image")["src"]
                    img_id = re.findall(r'id=(.*)&', img)[0]
                    if (os.path.isfile('img.jpg')):
                        os.remove('img.jpg')
                    if (os.path.isfile('img2.jpg')):
                        os.remove('img2.jpg')
                    with open('img.jpg', 'ab+') as f:
                        f.write(requests.get(img).content)
                        f.close()
                    print("* 验证码处理... *")
                    vcode_proc()
                    time.sleep(1)
                    img_code = vcode2str()
                    print("* 验证码：", img_code, '*')
                except:
                    print("* 无需验证码登录 *")
                    pass
                data = {
                    'captcha-id': img_id,
                    'captcha-solution': img_code,
                    'redir': 'https://www.douban.com/group/explore',
                    'form_email': '15797698335',
                    'form_password': '',  # !!!!!
                    'remember': 'on',
                    'login': '登录',
                    'source': 'group'
                }
                print("* 模拟登陆... *")
                cookie_login_flag = False
                ck = ''
                html_login = sess.post(url_login, data=data, headers=headers)
                if (html_login.status_code != 200):
                    print("* 访问错误: ", html_login.status_code, '*')
                    print("1小时后重试")
                    time.sleep(60 * 60)
                    continue
                if ("时光" in html_login.text):
                    break
                else:
                    print("* 验证码识别错误,状态重置 *")
                    time.sleep(5)

            if ("登录" in html_login.text):
                # cookie登录部分未用到，可做参考
                print("* 模拟登录失败，可能需要验证码登录 *")
                print("* Cookie登陆... *")
                url_cookie = "https://www.douban.com/group/topic/123635599/?start=0"
                sess = requests.session()
                header = {
                    'Cookie': 'bid=mTyCOa6IVcM; douban-fav-remind=1; __utmc=30149280; ll="118172"; ps=y; push_doumail_num=0;'
                              ' __utmv=30149280.18047; push_noty_num=0; ct=y; __utmz=30149280.1536643493.8.4.utmcsr=baidu|ut'
                              'mccn=(organic)|utmcmd=organic; ap_v=0,6.0; douban-profile-remind=1; dbcl2="180476760:hTTJHzKJ'
                              'PlY"; ck=54bX; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1536724818%2C%22https%3A%2F%2Fwww.bai'
                              'du.com%2Flink%3Furl%3DVTqGM3-_5EecWa3_9q8QsHk2YHCyWApWDP2V2PKhBMOSLo3D__zfgGXu-7Ni3JDq%26wd%3'
                              'D%26eqid%3Da000e2e700033ff6000000045b985c6b%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.707'
                              '823513.1533864750.1536721200.1536724839.12; _pk_id.100001.8cb4=010d889487409d0f.1533864750.11'
                              '.1536726397.1536722550.; __utmb=30149280.16.6.1536726397247'}
                html_cookie = sess.get(url_cookie)
                if ("时光" in html_cookie.text):
                    cookie_login_flag = True
                    print("* Cookie登录成功 *")
                    print("* 获取ck... *")
                    soup = BeautifulSoup(html_cookie.text, 'lxml')
                    ck = soup.find_all('tbody')[0].find_all("a")[-1]['href'][-4:]
                    print("* 获取成功ck: ", ck, "*")
            else:
                print("* 模拟登录成功 *")

            if (cookie_login_flag == False):
                print("* 获取ck... *")
                url_ck = "https://www.douban.com/group/topic/123635599/?start=0"
                html_ck = sess.get(url_ck, headers=headers)
                soup = BeautifulSoup(html_ck.text, 'lxml')
                ck = soup.find_all('tbody')[0].find_all("a")[-1]['href'][-4:]
                print("* 成功获取ck: ", ck, "*")

            print("* 开始刷留言...* ")
            start_flag = True
        if (start_flag == True):
            urls = [r'https://www.douban.com/group/topic/123637008',
                    r'https://www.douban.com/group/topic/123635599',
                    r'https://www.douban.com/group/topic/123634625',
                    r'https://www.douban.com/group/topic/123634843',
                    r'https://www.douban.com/group/topic/123634950'
                    ]
            url_len = len(urls)
            for i in range(url_len):
                url_group = urls[i] + r"/add_comment"
                pars = ["白日依山尽，黄河入海流。欲穷千里目，更上一层楼。 ",
                        "寥落古行宫，宫花寂寞红。白头宫女在，闲坐说玄宗。 ",
                        "三日入厨下，洗手作羹汤。未谙姑食性，先遣小姑尝。 ",
                        "君自故乡来，应知故乡事。来日绮窗前，寒梅著花未？ ",
                        "独坐幽篁里，弹琴复长啸。深林人不知，明月来相照。 ",
                        "床前明月光，疑是地上霜。举头望明月，低头思故乡。 ",
                        "移舟泊烟渚，日暮客愁新。野旷天低树，江清月近人。 "]
                one_par = pars[random.randint(0, len(pars) - 1)]
                Reload += 1
                try:
                    url_2 = urls[i]
                    url_img = sess.get(url_2, headers=headers)
                    soup = BeautifulSoup(url_img.text, 'lxml')
                    img = soup.find("img", id="captcha_image")["src"]
                    print("* 刷留言失败，可能需要验证码 *")
                    while 1:
                        img_code = ''
                        img_id = ''
                        print("* 获取验证码... *")
                        url_img = sess.get(url_2, headers=headers)
                        soup = BeautifulSoup(url_img.text, 'lxml')
                        img = soup.find("img", id="captcha_image")["src"]
                        if (img != ''):
                            img_id = re.findall(r'id=(.*)&', img)[0]
                            if (os.path.isfile('img.jpg')):
                                os.remove('img.jpg')
                            if (os.path.isfile('img2.jpg')):
                                os.remove('img2.jpg')
                            with open('img.jpg', 'ab+') as f:
                                f.write(requests.get(img).content)
                                f.close()
                            print("* 验证码处理... *")
                            vcode_proc()
                            time.sleep(1)
                            try_count = 0
                            retry_flag = False
                            while 1:
                                try:
                                    img_code = vcode2str()
                                    break
                                except:
                                    try_count += 1
                                    if (try_count > 3):
                                        print("* 验证码无法识别，将重新获取 *")
                                        retry_flag = True
                                        break
                                    time.sleep(1)
                                    pass
                            if (retry_flag == True):
                                continue
                            print("* 验证码：", img_code, '*')
                        data = {
                            'captcha-id': img_id,
                            'captcha-solution': img_code,
                            'ck': ck,
                            # 'ref_cid': '1692237050',
                            'rv_comment': one_par,
                            'start': 0,
                            'submit_btn': '发送',
                        }
                        html_group = sess.post(url_group, data=data, headers=headers, allow_redirects=False)
                        if (html_group.status_code == 200):
                            print("* 验证码识别错误,状态重置 *")
                        else:
                            break
                        start_flag = True
                except Exception as e:
                    print("## 此为验证信息，请忽略 -", e, "##")
                    print("* 留言无需验证码 *")
                    data = {
                        'ck': ck,
                        # 'ref_cid': '1692237050',
                        'rv_comment': one_par,
                        'start': 0,
                        'submit_btn': '发送',
                    }
                    html_group = sess.post(url_group, data=data, headers=headers)
                finally:
                    if (i == url_len - 1):
                        delay = random.randint(30, 60)
                        print("-> 全部发送成功,休息", delay, "分钟 - ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                        time.sleep(60 * delay)
                        return
                    print("* 第", i + 1, "个发送成功 *")
                    print("* 休息5s *")
                    time.sleep(5)
                    start_flag = True


def vcode_proc():
    img = Image.open(r'img.jpg').convert("L")
    pixdata = img.load()
    threshold = 21
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            count = 0
            if pixdata[x, y - 1] > 245:
                count = count + 1
            if pixdata[x, y + 1] > 245:
                count = count + 1
            if pixdata[x - 1, y] > 245:
                count = count + 1
            if pixdata[x + 1, y] > 245:
                count = count + 1
            if count > 2:
                pixdata[x, y] = 255
    img.save('img2.jpg')


def vcode2str():
    access_token = ""
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/webimage?access_token=' + access_token
    f = open(r'img2.jpg', 'rb')
    img = base64.b64encode(f.read())
    params = {"image": img}
    params = urllib.parse.urlencode(params).encode(encoding='UTF-8')
    request = urllib.request.Request(url, params)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib.request.urlopen(request)
    content = response.read()
    if (content):
        strings = eval(bytes.decode(content))
        try:
            words = strings["words_result"][0]['words']
            return words
        except Exception as e:
            print("* API接口调用出错：")
            print(strings)
            if (strings["error_code"] == 17):
                print("* 日调用次数已上限：", strings["error_msg"], "*\r\n")
                os._exit(0)


if __name__ == '__main__':
    while 1:
        main()