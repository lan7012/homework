import requests
from lxml import etree
import jieba
import numpy as np
import matplotlib.pyplot as plt
import time
from PIL import Image
from wordcloud import WordCloud


def GetData(forumdata):
    for j in forumdata:
        url = 'https://www.52pojie.cn/forum-x-1'
        url = url.split('-')
        nurl = url[0] + '-' + j + '-' + url[2] + '.html'
        html = requests.get(nurl)
        ehtml = etree.HTML(html.text)
        forumname = ''.join(ehtml.xpath('//*[@id="ct"]/div/div[1]/div[1]/h1/a/text()')).replace('『', '').replace('』',
                                                                                                                 '')
        print(forumname)
        pagenum = ehtml.xpath('//*[@id="fd_page_top"]/div/label/span/text()')
        pagenum = pagenum[0].replace(' / ', '').replace(' 页', '')
        txt = ''
        for i in range(1, int(pagenum) + 1):
            nurl = url[0] + '-' + j + '-' + str(i) + '.html'
            html = requests.get(nurl)
            ehtml = etree.HTML(html.text)
            # pltxt = ' '.join(ehtml.xpath('//*[@id="threadlisttableid"]/tbody/tr/td[2]/cite/a/text()'))#获取帖子作者
            pltxt = ' '.join(ehtml.xpath('//*[@class="s xst"]/text()'))  # 帖子标题
            txt = txt + pltxt
            time.sleep(1)  # 给服务器留些喘气的时间
        cut_text = txt
        wordcloud = WordCloud(
            font_path='simhei.ttf',
            background_color='white',
            width=800,
            height=500
        ).generate(cut_text)
        wordcloud.to_file('c:\\' + forumname + '.png')
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()


if __name__ == '__main__':
    forumdata = [
        "2",  # 原创发布区 0
        "5",  # 脱壳破解区 1
        "65",  # 移动安全区 2
        "59",  # 软件调试区 3
        "24",  # 编程语言区 4
        "6",  # 动画发布区 5
        "4",  # 逆向资源区 6
        "16",  # 精品软件区 7
        "8",  # 悬赏问答区 8
        "32",  # 病毒分析区 9
        "50",  # 病毒救援区 10
        "41"  # 安全工具区 11
    ]
    print('开始获取,请稍候...')
    GetData(forumdata)