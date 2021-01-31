from common import method  #导入公共方法
from test_data import test_data  # 导入数据
from selenium import webdriver
driver=webdriver.Chrome()  # 初始化一个浏览器
driver.implicitly_wait(5)  # 隐性等待
url=test_data.data['url']
username=test_data.data.get('username')
password=test_data.data.get('password')
key=test_data.data.get('key')
num = method.search_fun(driver,url,username,password,key)
if key in num:
    print("执行用例通过")
else:
    print("执行用例不通过")