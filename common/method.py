# 封装函数
# 封装函数三部曲 1.写好代码  2.参数化
# 打开页面
import time
def open_url(driver,url):
    driver.get(url)
    driver.maximize_window()

# 登陆页面
def login_fun(driver,username,password):
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    # 勾选记住密码
    driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()
    driver.find_element_by_id("btnSubmit").click()

# 搜索  搜索是一个综合性的函数，所以要调用前两个函数
def search_fun(driver,url,username,password,key):
    open_url(driver,url)
    login_fun(driver,username,password)
    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    #先切换到该页面中  从页面分析得出此时的id是动态的，不能和直接定位 ，可以找下一级
    id_li = driver.find_element_by_xpath('//div[text()="零售出库"]//..').get_attribute('id')  # 通过定位获取id  然后在进行拼接
    id_frame =id_li +"-frame"
    # 方法一 通过id属性
    # driver.switch_to.frame(id_frame)
    #方法二：通过xpath
    driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@id="{}"]'.format(id_frame)))
    driver.find_element_by_id("searchNumber").send_keys(key)
    driver.find_element_by_id("searchBtn").click()
    # 获取单据的文本
    time.sleep(2)
    num = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text
    # print(num)
    # 判断
    # if '841' in num:
    #     print("执行用例通过")
    # else:
    #     print("搜索失败！")
    return num


