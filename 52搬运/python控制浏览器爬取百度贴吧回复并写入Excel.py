# http://tieba.baidu.com/i/i/my_reply
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import xlwt


def login(name, passwd):
    # 1.打开浏览器
    driver = webdriver.Chrome()
    # 2.设置地址
    url = "https://www.baidu.com/"
    # 3.访问网址
    driver.get(url)
    # 4.分析网页，找到登录元素
    # login = driver.find_elements_by_id('u1').find_elements_by_class_name('lb')[0]   #方法一
    login = driver.find_elements_by_css_selector('div[id=u1] a[class=lb]')[0]  # 方法二
    # 5.点击登录按钮
    login.click()
    time.sleep(2)
    changeusename = driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn")
    changeusename.click()
    # 点击之后要加等待时间
    time.sleep(2)
    # 8.找到 输入 用户名 和密码框，并且设置内容
    # <input id="TANGRAM__PSP_10__userName">
    username = driver.find_element_by_id('TANGRAM__PSP_10__userName')
    # 输入账号名
    username.send_keys(name)
    time.sleep(1)
    # <input id="TANGRAM__PSP_10__password">
    password = driver.find_element_by_id('TANGRAM__PSP_10__password')
    # 输入密码
    password.send_keys(passwd)
    time.sleep(2)
    # <input id="TANGRAM__PSP_10__submit">
    submit = driver.find_element_by_id('TANGRAM__PSP_10__submit')
    submit.click()
    return driver


def opentieba(browser, url='http://tieba.baidu.com/i/i/my_reply?&pn=1'):
    browser.get(url)
    context = browser.page_source
    soup = BeautifulSoup(context, 'html.parser')
    context = browser.find_element_by_css_selector(".simple_block_container")
    print(context.text)
    cont = soup.find_all(class_='b_right_up')
    return cont


def writeXls(cont):
    i = 0  # 从第几行开始写
    # 1、导入模块    　　
    # 2、创建workbook（其实就是excel，后来保存一下就行）
    # workbook = xlwt.Workbook(encoding='ascii')
    workbook = xlwt.Workbook(encoding='utf-8')
    # 3、创建表
    worksheet = workbook.add_sheet('sheet1')
    for link in cont:
        print(link)
        item = BeautifulSoup(str(link), 'html.parser')
        reply_context = item.find(class_="for_reply_context")
        thread_title = item.find(class_="thread_title")
        href = str(thread_title)[31:54]
        href = 'http://tieba.baidu.com/' + href
        print(reply_context.text)
        worksheet.write(i, 0, label=reply_context.text)
        print(thread_title.text)
        worksheet.write(i, 1, xlwt.Formula('HYPERLINK("' + href + '"," ' + thread_title.text + '")'))
        print(href)
        i = i + 1
        time.sleep(1)

    # 5、保存
    date = time.strftime("%Y%m%d%H%M%S", time.localtime()) + '_'
    workbook.save('Excel_' + date + str(i) + '.xls')
    i = 0
    return "successful"


def writedata(data):
    # 1、导入模块    　　
    # 2、创建workbook（其实就是excel，后来保存一下就行）
    workbook = xlwt.Workbook(encoding='ascii')
    # 3、创建表
    worksheet = workbook.add_sheet('sheet1')
    # 4、往单元格内写入内容
    worksheet.write(0, 0, label=data)
    # 5、保存
    workbook.save('Excel_Workbook.xls')


def main():
    driver = login("美食拍客136822", "*****")
    str = input("请输入任意内容确认你已经登录：")
    xlscontext = opentieba(driver, url='http://tieba.baidu.com/i/i/my_reply?&pn=1')
    res = writeXls(xlscontext)
    print(res)


if __name__ == '__main__':
    main()