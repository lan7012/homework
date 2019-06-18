import json
import requests
from multiprocessing import Queue
from handel_mongo import mongo_info
from concurrent.futures import ThreadPoolExecutor

#创建队列
queue_list = Queue()

def handel_request(url, data):
    header = {
        "client":"4",
        "version":"6922.2",
        "device":"SM-G955F",
        "sdk":"19,4.4.2",
        "imei":"355757010002166",
        "channel":"zhuzhan",
        #"mac":"00:D8:61:38:38:63",
        "resolution":"1280*720",
        "dpi":"1.5",
        #"android-id":"00d8613838639261",
        #"pseudo-id":"1383863926100d86",
        "brand":"samsung",
        "scale":"1.5",
        "timezone":"28800",
        "language":"zh",
        "cns":"3",
        "carrier":"CMCC",
        #"imsi":"460070021661383",
        "user-agent":"Mozilla/5.0 (Linux; Android 4.4.2; SM-G955F Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36",
        "reach":"1",
        "newbie":"1",
        #"lon":"107.568699",
        #"lat":"39.00266",
        #"cid":"150600",
        "Content-Type":"application/x-www-form-urlencoded; charset=utf-8",
        "Accept-Encoding":"gzip, deflate",
        "Connection":"Keep-Alive",
        #"Cookie":"duid=60207784",
        "Host":"api.douguo.net",
        #"Content-Length":"68",
    }
    response = requests.post(url=url, headers=header, data=data)
    return response

def urld():
    url = 'http://api.douguo.net/recipe/flatcatalogs'
    data = {
        "client": "4",
        #"_session": "1560859414785355757010002166",
        #"v": "1503650468",
        "_vs": "2305",
    }

    response = handel_request(url=url, data=data)
    index_response_dict = json.loads(response.text)
    for index_item in index_response_dict['result']['cs']:
        for index_item_1 in index_item['cs']:
            for index_item_2 in index_item_1['cs']:
                data_2 = {
                    "client": "4",
                    #"_session": "1560859414785355757010002166",
                    "keyword": index_item_2['name'],
                    "order": "3",
                    "_vs": "400",
                }
                queue_list.put(data_2)

def handle_caipu_list(data):
    print('当前处理的食材：', data['keyword'])
    caipu_list_url = 'http://api.douguo.net/recipe/v2/search/0/20'
    caipu_list_response = handel_request(url=caipu_list_url, data=data)
    caipu_list_response_dict = json.loads(caipu_list_response.text)
    for item in caipu_list_response_dict['result']['list']:
        caipu_info = {}
        caipu_info['shicai'] = data['keyword']
        if item['type'] == 13:
            caipu_info['user_name'] = item['r']['an']
            caipu_info['shicai_id'] = item['r']['id']
            caipu_info['shicai_cookstory'] = item['r']['cookstory'].replace("\n", "").replace(" ", "")
            caipu_info['caipu_name'] = item['r']['n']
            caipu_info['zhuoliao'] = item['r']['major']
            zuofa_url = 'http://api.douguo.net/recipe/detail/'+str(caipu_info['shicai_id'])
            zuofa_data = {
                "client": "4",
                #"_session": "1560859414785355757010002166",
                "author_id": "0",
                "_vs": "2801",
                "_ext": '{"query":{"id":'+str(caipu_info['shicai_id'])+',"kw":'+data['keyword']+',"idx":"1","src":"2801","type":"13"}}'
            }
            detail_response = handel_request(url=zuofa_url, data=zuofa_data)
            detail_response_dict = json.loads(detail_response.text)
            caipu_info['tips'] = detail_response_dict['result']['recipe']['tips']
            caipu_info['cookstep'] = detail_response_dict['result']['recipe']['cookstep']
            print("当前入库的菜谱：", caipu_info["caipu_name"])
            mongo_info.insert_item(caipu_info)
        else:
            continue

urld()
pool = ThreadPoolExecutor(max_workers=20)
while queue_list.qsize() > 0:
    pool.submit(handle_caipu_list, queue_list.get())
