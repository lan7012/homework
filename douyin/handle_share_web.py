import requests
import re
from lxml import etree
from douyin.handle_db(1) import handle_get_task

def handle_decode(input_data):
    search_douyin_str = re.compile(r'抖音ID：')
    #抖音web分享界面数字破解列表
    regex_list = [
        {'name': ['&#xe603; ', '&#xe60d; ', '&#xe616; '], 'value': 0},
        {'name': ['&#xe602; ', '&#xe60e; ', '&#xe618; '], 'value': 1},
        {'name': ['&#xe605; ', '&#xe610; ', '&#xe617; '], 'value': 2},
        {'name': ['&#xe604; ', '&#xe611; ', '&#xe61a; '], 'value': 3},
        {'name': ['&#xe606; ', '&#xe60c; ', '&#xe619; '], 'value': 4},
        {'name': ['&#xe607; ', '&#xe60f; ', '&#xe61b; '], 'value': 5},
        {'name': ['&#xe608; ', '&#xe612; ', '&#xe61f; '], 'value': 6},
        {'name': ['&#xe60a; ', '&#xe613; ', '&#xe61c; '], 'value': 7},
        {'name': ['&#xe60b; ', '&#xe614; ', '&#xe61d; '], 'value': 8},
        {'name': ['&#xe609; ', '&#xe615; ', '&#xe61e; '], 'value': 9},
    ]

    for i1 in regex_list:
        for i2 in i1['name']:
            input_data = re.sub(i2, str(i1['value']), input_data)

    #构造成HTML结构
    share_web_html = etree.HTML(input_data)
    #数据字典
    user_info = {}
    user_info['nickname'] = share_web_html.xpath("//p[@class='nickname']/text()")
    douyin_id1 = share_web_html.xpath("//p[@class='shortid']/text()")[0].replace(' ', '')
    douyin_id2 = ''.join(share_web_html.xpath("//p[@class='shortid']/i/text()")).replace(' ', '')
    user_info['shortid'] = re.sub(search_douyin_str, '', douyin_id1+ douyin_id2)
    try:
        user_info['job'] = share_web_html.xpath("//span[@class='info']/text()")[0].replace(' ', '')
    except:
        pass
    user_info['describe'] = share_web_html.xpath("//p[@class='signature']/text()")[0]
    user_info['guanzhu'] = share_web_html.xpath("//p[@class='follow-info']/span[1]/span/i/text()")[0].replace(' ', '')
    user_info['follower'] = ''.join(share_web_html.xpath("//p[@class='follow-info']/span[2]/span/i/text()")).replace(' ', '')
    danwei1 = share_web_html.xpath("//p[@class='follow-info']/span[2]/span[@class='num']/text()")[-1]
    if danwei1.strip() == 'w':
        user_info['follower'] = str(int(user_info['follower'])/ 10)+ 'w'
    user_info['zan'] = ''.join(share_web_html.xpath("//p[@class='follow-info']/span[3]/span/i/text()")).replace(' ', '')
    danwei2 = share_web_html.xpath("//p[@class='follow-info']/span[3]/span[@class='num']/text()")[-1]
    if danwei2.strip() == 'w':
        user_info['zan'] = str(int(user_info['zan'])/ 10)+ 'w'

    print(user_info)

def handle_douyin_web_share(task):
    share_web_url = 'https://www.iesdouyin.com/share/user/%s'%task['share_id']
    share_web_header = {
        "user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }

    #请求回来的文本数据
    share_web_response = requests.get(url=share_web_url, headers=share_web_header)
    #进行破解
    handle_decode(share_web_response.text)

task = handle_get_task()
handle_douyin_web_share(task)