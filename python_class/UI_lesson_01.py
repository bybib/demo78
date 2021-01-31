# 从selenium这个工具里面导入webdriver这个库
from selenium import webdriver
import time
driver = webdriver.Chrome()  # 初始化一个浏览器
driver.get("https://taobao.com")  # 打开浏览器对应的网址
# 浏览器最大化
driver.maximize_window()
#
driver.get("https://baidu.com")
# 返回上一个界面
time.sleep(2)
driver.back()
time.sleep(2)
# 前进一个界面
driver.forward()
time.sleep(2)
# 刷新
driver.refresh()
