# 接口测试
# 注册接口
import requests, pprint, jsonpath # 导入requests模块
# url_api_register = "http://8.129.91.152:8766/futureloan/member/register"
# api_data_register = {
#   "mobile_phone": "13668832334",
#   "pwd": "lemon12348",
#   "type": "0",
#   "reg_name": "管理员用户lemon"
# }
# head_register = {"X-Lemonban-Media-Type": "lemonban.v2",
#         "Content-Type": "application/json"}
# response = requests.post(url=url_api_register, json=api_data_register, headers=head_register)
# print(response.json())  # 查看响应结果的格式
# 登陆接口
url_api_login = "http://8.129.91.152:8766/futureloan/member/login"
api_data_login = {
  "mobile_phone": "13668832334",
  "pwd": "lemon12348"
}
head_login = {"X-Lemonban-Media-Type": "lemonban.v2"}
response = requests.post(url=url_api_login, json=api_data_login,headers=head_login)
# pprint.pprint(response.json())
res = response.json()  # 赋值于一个变量，为下面充值 接口方便
# 充值接口
# 方法一
# member_id = res["data"]["id"]  #取出id的值
# # print(member_id)
# token = res["data"]["token_info"]["token"]  #取出token
# # print(token)
# url_api_recharge = "http://8.129.91.152:8766/futureloan/member/recharge"
# api_data_recharge ={
#   "member_id": member_id,
#   "amount": "0.01"
# }
# head_recharge = {"X-Lemonban-Media-Type": "lemonban.v2",
#         "ontent-Type": "application/json",
#         "Authorization": "Bearer "+token}  #字符串拼接token
# response = requests.post(url=url_api_recharge, json=api_data_recharge, headers=head_recharge)
# pprint.pprint(response.json())

# 方法二 jsonpath
member_id = jsonpath.jsonpath(res, "$.data.id")[0]  #取出id的值    json提取器   第一个参数为变量名  同( res,$..id )
print(member_id)
token = jsonpath.jsonpath(res, "$.data.token_info.token")[0]  #取出token 进行取值，后面只有一个元素所以下标为0
print(token)
url_api_recharge = "http://8.129.91.152:8766/futureloan/member/recharge"
api_data_recharge ={
  "member_id": member_id,
  "amount": "0.01"
}
head_recharge = {"X-Lemonban-Media-Type": "lemonban.v2",
        "ontent-Type": "application/json",
        "Authorization": "Bearer "+token}  #字符串拼接token
response = requests.post(url=url_api_recharge, json=api_data_recharge, headers=head_recharge)
pprint.pprint(response.json())


# 访问百度请求内容
url_baidu = "https://www.baidu.com/"
# 以字典的格式传头过去
# User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36
head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
response = requests.get(url=url_baidu,headers = head)
# pprint.pprint(response.text)  #自动解码页面，如果不能成功可以用.content.decode("utf8")解码
# 手动解码
pprint.pprint(response.content.decode("utf8"))