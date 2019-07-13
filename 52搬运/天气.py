from tkinter import *
import tkinter as tk
import requests
from PIL import ImageTk as itk


class MyFrame(Frame):
    def __init__(self):
        self.root = Tk()

        self.root.title("天气查询")
        self.root.geometry('1200x700+400+220')

        bg = tk.Canvas(self.root, width=1200, height=600, bg='white')
        self.img = itk.PhotoImage(file="bg.gif")
        bg.place(x=100, y=40)
        bg.create_image(0, 0, anchor=NW, image=self.img)

        self.city = Entry(self.root, width=16, font=("仿宋", 18, "normal"))
        self.city.place(x=200, y=60)

        citylabel = Label(self.root, text='查询城市', font=("仿宋", 18, "normal"))
        citylabel.place(x=80, y=60)

        # 查询按钮
        chaxun = Button(self.root, width=10, height=3, text="查询", bg='#00CCFF', bd=5, font="bold")
        chaxun.bind("<Button-1>", self.search)
        chaxun.place(x=800, y=50)

        self.result = Listbox(self.root, heigh=18, width=65, font=("仿宋", 20, "normal"))  # 显示天气框
        self.result.place(x=125, y=120)

    def tianqiforecast(self, searchcity):
        print('请输入所要查询天气的城市：')
        city = searchcity
        # city='minquan'
        url = 'http://toy1.weather.com.cn/search?cityname=' + city + '&callback=success_jsonpCallback&_=1548048506469'
        # print(url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Cookie': '__guid=182823328.3322839646442213000.1543932524694.901; vjuids=1858d43b6.167798cbdb7.0.8c4d7463d5c5d; vjlast=1543932526.1543932526.30; userNewsPort0=1; f_city=%E5%B9%B3%E9%A1%B6%E5%B1%B1%7C101180501%7C; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1543932526,1543932551,1543932579; Wa_lvt_1=1547464114,1547464115,1547880054,1547983123; defaultCty=101181001; defaultCtyName=%u5546%u4E18; monitor_count=6; Wa_lpvt_1=1547983809'
        }
        response = requests.get(url, headers=headers)
        html1 = response.content.decode('utf-8')
        # print(html)

        citys = re.findall('"ref":"(.*?)~.*?~(.*?)~.*?~(.*?)~.*?~.*?~.*?~.*?~(.*?)"', html1, re.S)
        if (len(citys) == 0):
            print('未查找到该城市')
            exit(-5)
        for i in range(0, len(citys)):
            print(i + 1, ':%14s%14s%14s%14s ' % (citys[0], citys[3], citys[2], citys[1]))
        # choose = int(input('请选择城市编号：[1~' + str(len(citys)) + ']\n'))
        choose = 1
        if (len(citys[choose - 1][0]) == 9):
            if (citys[choose - 1][0][0] != '1' or citys[choose - 1][0][1] != '0' or citys[choose - 1][0][2] != '1'):
                print('暂时无法查询国外天气,程序已退出')
                exit(404)
            else:
                url2 = 'http://www.weather.com.cn/weathern/' + citys[choose - 1][0] + '.shtml'


responseweather = requests.get(url2, headers=headers)
html2 = responseweather.content.decode('utf-8')

weather = re.findall('<li class="date-.*?".*?".*?">(.*?)</.*?"date-i.*?">(.*?)<.*?', html2, re.S)
weather.append(re.findall(
    '<p class="weather-in.*?" title="(.*?)".*?title="(.*?)".*?title="(.*?)".*?<p class="wind-i.*?">(.*?)</p>',
    html2, re.S))
Hightempture = re.findall(
    '<script>var eventDay =\["(.*?)","(.*?)","(.*?)","(.*?)","(.*?)","(.*?)","(.*?)","(.*?)"\];', html2,
    re.S)
Lowtempture = re.findall(
    'var eventNight =\["(.*?)","(.*?)","(.*?)","(.*?)","(.*?)","(.*?)","(.*?)","(.*?)"\];',
    html2, re.S)
# print(Hightempture,Lowtempture)
b = '查询城市为：' + str(citys[choose - 1][3]) + '    ' + str(citys[choose - 1][1])
self.result.insert(END, b)
for i in range(0, 8):
    # print(weather)
    '''print("%4s%4s%10s\t\t\t%s℃ ~ %s℃\t\t\t%s%s%-s" % (
        weather[0], weather[1], weather[8][0], Lowtempture[0], Hightempture[0],
        weather[8][1],
        weather[8][3], weather[8][2]))'''
a = weather[0] + '    ' + weather[1] + '    ' + weather[8][0] + '    ' + Lowtempture[0] + '℃  ~  ' + \
    Hightempture[0] + '℃   ' + weather[8][1] + weather[8][3] + weather[8][2]
self.result.insert(END, a)

if (len(citys[choose - 1][0]) == 12):
    url2 = 'http://forecast.weather.com.cn/town/weathern/' + citys[choose - 1][0] + '.shtml'
responseweather = requests.get(url2, headers=headers)
html2 = responseweather.content.decode('utf-8')

weather = re.findall('<li class="date-.*?".*?"da.*?">(.*?)</.*?"date-i.*?">(.*?)<.*?', html2, re.S)

html2 = re.sub('lt;', '<', html2)
weather.append(re.findall(
    '<p class="weather-in.*?" title="(.*?)".*?title="(.*?)".*?title="(.*?)".*?<p class="wind-i.*?">\\r\\n(.*?)\\r\\n',
    html2, re.S))

Hightempture = re.findall(
    'var eventDay = \["(.*?)","(.*?)","(.*?)","(.*?)","(.*?)","(.*?)","(.*?)","(.*?)"\];', html2, re.S)

Lowtempture = re.findall(
    'var eventNight = \["(.*?)","(.*?)","(.*?)","(.*?)","(.*?)","(.*?)","(.*?)","(.*?)"\];',
    html2, re.S)
# print(Hightempture,Lowtempture)
b = '查询城市为：' + str(citys[choose - 1][3]) + '   ' + str(citys[choose - 1][2]) + '    ' + str(citys[choose - 1][1])
self.result.insert(0, b)
# print(weather[8][2])
# print(weather)
for i in range(0, 8):
    # print(weather)
    '''print("%4s%4s%10s\t\t\t%s℃ ~ %s℃\t\t\t%s%s%-s" % (
        weather[0], weather[1], weather[8][0], Lowtempture[0], Hightempture[0],
        weather[8][1],
        weather[8][3], weather[8][2]))'''
a = weather[0] + '    ' + weather[1] + '    ' + weather[8][0] + '    ' + Lowtempture[0] + '℃  ~  ' + \
    Hightempture[0] + '℃   ' + weather[8][1] + weather[8][3] + weather[8][2]
self.result.insert(END, a)


def search(self, event):
    mycity = self.city.get()
    if (mycity != ''):
        self.result.delete(0, END)
        self.city.delete(0, END)
        self.tianqiforecast(mycity)


if __name__ == '__main__':
    myframe = MyFrame()
    myframe.root.mainloop()