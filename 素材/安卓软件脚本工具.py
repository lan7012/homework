from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

#获取安卓软件
#系统、安卓版本、模拟器或手机名字、软件pack、activity
cap = {
  "platformName": "Android",
  "plartformVersion": "",
  "deviceName": "",
    #安装包放入SDK目录下，拖动到appt.exe
    #运行命令 C:\SDK\build-tools\29.0.0>aapt.exe dump badging 安装包拖动
  "appPackage": "",
  "appActivity": "",
    #记录启动app的行为（跳过、版本升级）
  "noReset": True
}
#本地客户端连接
driver = webdriver.Remote("http://localhost:4723/wd/hub", cap)

def get_size():
  x = driver.get_window_size()['width']
  y = driver.get_window_size()['height']
  return (x, y)

#点击操作，延迟2秒，用u工具抓取xpath信息
try:
    #如果出现这个
  if WebDriverWait(driver,2).until(lambda x:x.find_element_by_xpath("")):
    #就是执行这个
    driver.find_element_by_xpath("").click()
except:
  pass

#输入操作
try:
    #如果出现这个
  if WebDriverWait(driver,2).until(lambda x:x.find_element_by_xpath("")):
    #就在这输入这个
    driver.find_element_by_xpath("").send_keys("")
    #增加点击
    driver.find_element_by_xpath("").click()
except:
  pass

#滑动操作
#如果出现这个
if WebDriverWait(driver,2).until(lambda x:x.find_element_by_xpath("")):
#点击进去
  driver.find_element_by_xpath("").click()
#进行滑动
  l = get_size()

  x1 = int(l[0] * 0.5)
  y1 = int(l[1] * 0.75)
  y2 = int(l[1] * 0.25)

  while True:
#滑动延迟
    time.sleep(1)
    driver.swipe(x1, y1, x1, y2)