from selenium import webdriver
import time
driver = webdriver.Chrome()  # 初始化一个浏览器
driver.get("http://erp.lemfix.com/login.html")
driver.maximize_window()
# 获取页面的标题
page_title = driver.title
# 判断页面中是否包含标题
if page_title =="柠檬ERP":
    print("这个页面的标题是：{}".format(page_title))
else:
    print("该条用例不通过！")
# 用例操作，输入用户名和密码。点击登陆
driver.find_element_by_id("username").send_keys("test123")
driver.find_element_by_id("password").send_keys("123456")
# 勾选记住密码
driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()
driver.find_element_by_id("btnSubmit").click()
# /html/body/div[1]/aside/div/section/div[1]/div[2]/p

# 确认登陆用户名
time.sleep(3)
page_name = driver.find_element_by_xpath("//p").text     #获取这个元素的文本内容
# 判断
if page_name =="测试用户":
    print("这个登陆用户是：{}".format(page_name))
else:
    print("这个用例不通过！")


# 点击零售出库
driver.find_element_by_xpath("//span[text()='零售出库']").click()
#先切换到该页面中  从页面分析得出此时的id是动态的，不能和直接定位 ，可以找下一级
id_li = driver.find_element_by_xpath('//div[text()="零售出库"]//..').get_attribute('id')  # 通过定位获取id  然后在进行拼接
id_frame =id_li +"-frame"
# 方法一 通过id属性
# driver.switch_to.frame(id_frame)
#方法二：通过xpath
driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@id="{}"]'.format(id_frame)))
driver.find_element_by_id("searchNumber").send_keys("841")
driver.find_element_by_id("searchBtn").click()
# 获取单据的文本
time.sleep(2)
num = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text
# print(num)
# 判断
if '841' in num:
    print("执行用例通过")
else:
    print("搜索失败！")


