import json
import os
import re
import shutil

import requests
from lxml import etree


class MKSpider:

    def __init__(self):
        self.search_url = "https://www.mkzhan.com/search/?keyword={}"
        self.per_chapter_url = "https://comic.mkzcdn.com/chapter/?comic_id={}"
        self.chapter_url = "https://www.mkzhan.com/{}/{}.html"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }
        self.cid = None
        self.cid_list = []
        self.cartoons_dict = None
        self.cartoon_name = None

    # 获取搜索的漫画id
    def search_cartoon(self):
        cartoon_name = input("请输入你需要下载的漫画:")
        response = requests.get(self.search_url.format(cartoon_name), headers=self.headers).content.decode()
        # 判断是否存在
        search_count = re.search('<div class="search-page-wr" data-count="(\d+)">', response).group(1)
        if search_count == "0":
            print('很遗憾，您搜索的内容暂时没有找到，我们为您推荐了以下漫画~')
        else:
            print("“{}”---搜索结果{}个".format(cartoon_name, search_count))
        data_cid_list = re.findall('<div class="common-comic-item" data-cid="(\d+)">', response)
        title_list = re.findall('<p class="comic__title"><a href=".*?">(.+)</a></p>', response)  # 哆啦A梦   海贼王   绝色医妃
        self.cartoons_dict = {}
        print('id为漫画id,title为漫画名')
        for cid in data_cid_list:
            self.cartoons_dict[cid] = title_list[data_cid_list.index(cid)]
            print("id:{}, title:{}".format(cid, title_list[data_cid_list.index(cid)]))
        while True:
            cid = input('请输入你需要下载的漫画id:')
            if cid in self.cartoons_dict.keys():
                self.cid = cid
                self.cartoon_name = self.cartoons_dict[cid]
                if os.path.exists(self.cartoon_name):
                    shutil.rmtree(self.cartoon_name)
                os.mkdir(self.cartoon_name)
                break

    # 获取漫画章节
    def get_cartoon_chapter(self):
        response = requests.get(self.per_chapter_url.format(self.cid), headers=self.headers).content.decode()
        chapter_list = json.loads(response)["data"]
        chapter_id_list = []
        for chapter in chapter_list:
            chapter_id_list.append(chapter['chapter_id'])
        print(chapter_id_list)
        print(len(chapter_id_list))
        return chapter_id_list

    # 获取图片数据
    def get_image_data(self, url):
        return requests.get(url, headers=self.headers).content

    # 获取每章的图片地址
    def title_image_url(self, chapter_id):
        response = requests.get(self.chapter_url.format(self.cid, chapter_id), headers=self.headers).content.decode()
        html = etree.HTML(response)
        img_list = html.xpath('//img[@class="lazy-read"]/@data-src')
        title = html.xpath('//a[@class="last-crumb"]/text()')[0]
        # print(img_list)
        # print(title)
        # print(len(img_list))
        return title, img_list

    def mkdir(self, title):
        if os.path.exists(self.cartoon_name + "/" + title):
            print(self.cartoon_name)
            shutil.rmtree(self.cartoon_name + "/" + title)
        os.mkdir(self.cartoon_name + "/" + title)

    # 保存图片
    def save(self, title, i, img_data):
        # print(img_data)
        # print(title)
        # print(self.cartoon_name)
        with open(self.cartoon_name + "/" + title + '/' + str(i) + '.jpg', 'wb') as image:
            image.write(img_data)

    # 程序运行中心
    def run(self):
        self.search_cartoon()
        chapter_id_list = self.get_cartoon_chapter()
        for chapter_id in chapter_id_list[0:2]:
            title, img_list = self.title_image_url(chapter_id)
            self.mkdir(title)
            i = 1
            for img_url in img_list:
                print(img_url)
                img_data = self.get_image_data(img_url)
                self.save(title, i, img_data)
                i += 1


if __name__ == '__main__':
    MKSpider().run()
