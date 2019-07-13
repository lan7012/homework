# coding:utf-8
#双线程边下边播图片
from requests import get
from bs4 import BeautifulSoup
import os
import cv2
from threading import Thread
from time import sleep

scroll_index = 0
pic_index = 0


def show_img(path):
    img = cv2.imread(path)
    height, width = img.shape[:2]
    size = (int(width * 0.6), int(height * 0.6))
    shrink = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
    cv2.imshow('image', shrink)
    cv2.waitKey(1000)


def scroll_show():  # pic_total
    global scroll_index, pic_index
    while 1:
        if scroll_index < pic_index:
            print("播放图[%d]" % scroll_index)
            show_img(str(scroll_index) + r'.jpg')
            scroll_index += 1
        else:
            sleep(1)


def download_img():
    global scroll_index, pic_index
    url = r'https://www.mzitu.com/zipai/'
    headers = {
        'Referer': 'https://www.mzitu.com/zipai/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    }
    html = get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
    pages = int(soup.find(class_='page-numbers current').string)
    page_index = pages
    pic_index = 0
    for t in range(pages):
        url_new = r'https://www.mzitu.com/zipai/comment-page-%d/#comments' % page_index
        page_index -= 1
        print("访问地址:", url_new)
        html = get(url_new, headers=headers)
        soup = BeautifulSoup(html.text, 'lxml')
        items = soup.find_all('img', class_='lazy')
        items_len = len(items)
        print("本页[%d]张" % items_len)
        for i in range(items_len):
            pic_response = get(items[i]['data-original'], headers=headers)
            with open(str(pic_index) + r'.jpg', 'wb') as f:
                f.write(pic_response.content)
            print("图[%d]下载完成" % pic_index)
            pic_index += 1
        print('*' * 50)
    return pic_index


def main():
    global scroll_index, pic_index
    try:
        print("创建目录")
        os.mkdir(os.getcwd() + r'\pic')
    except:
        print("目录存在")
    os.chdir(os.getcwd() + r'\pic')
    print("文件路径:", os.getcwd())

    scroll_index = 0
    download_thread = Thread(target=download_img)
    scroll_thread = Thread(target=scroll_show)
    download_thread.start()
    scroll_thread.start()
    download_thread.join()
    scroll_thread.join()

    cv2.destroyAllWindows()
    os._exit(0)


if __name__ == '__main__':
    main()