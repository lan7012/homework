from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

cap = {
  "platformName": "Android",
  "plartformVersion": "4.4.2",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "com.tal.kaoyan",
  "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
  "noReset": True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", cap)

def get_size():
  x = driver.get_window_size()['width']
  y = driver.get_window_size()['height']
  return (x, y)

try:#跳过广告
  if WebDriverWait(driver,2).until(lambda x:x.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_skip']")):
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_skip']").click()
except:
  pass

try:#输入账号密码
  if WebDriverWait(driver,2).until(lambda x:x.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_email_edittext']")):
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_email_edittext']").send_keys("ceshi12355")
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_password_edittext']").send_keys("ceshi123")
    driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.tal.kaoyan:id/login_login_btn']").click()
except:
  pass

try:#点击确定
  if WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tip_commit']")):
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tip_commit']").click()
except:
  pass

try:#点击X
  if WebDriverWait(driver,3).until(lambda x:x.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.tal.kaoyan:id/view_wemedia_image']")):
    driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.tal.kaoyan:id/view_wemedia_cacel']").click()
except:
  pass

try:#点击同意
  if WebDriverWait(driver,2).until(lambda x:x.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_agree']")):
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_agree']").click()
    driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.RelativeLayout[3]").click()
except:
  pass

#点击研讯
if WebDriverWait(driver,2).until(lambda x:x.find_element_by_xpath("//android.support.v7.widget.RecyclerView[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.RelativeLayout[3]")):
  driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.RelativeLayout[3]/android.widget.LinearLayout[1]").click()

  l = get_size()

  x1 = int(l[0] * 0.5)
  y1 = int(l[1] * 0.75)
  y2 = int(l[1] * 0.25)

  while True:
    time.sleep(1)
    driver.swipe(x1, y1, x1, y2)