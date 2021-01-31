# for i in range(0,8):
#     print(i)

#
# num1 = str(input("请输入一个数字: "))
# if num1.isdigit():
#     if int(num1) % 2 == 0:
#         print("True")
#     else:
#         print("Flase")1
# else:
#     print("请输入一个数字")



# 设计一个函数，获取一个100以内偶数的纯数字序列，并存到列表里， 然后求这些偶数数字的和。
# def add_fun(num1):
#     num =0
#     list = []
#     for i in range(2,num1,2):
#         # print(i)
#         list.append(i)
#         num += i
#     return num,list
# result = add_fun(100)
# print("100以内偶数的和为{},\n生成的偶数列表为{}".format(result[0],result[1]))
"""
某比赛需要获取你的个人信息，设计一个程序，运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据存储起来，

    2、数据存储完了，然后输出个人介绍，格式如下:  我的名字XXX，今年XXX岁，性别XX，喜欢敲代码

    3. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；

    4, 平台为了保护你的隐私，需要你删除你的联系方式；...
"""
dict1 = dict(name = input('请输入你的名字：'),

             gender = input('请输入你的性别：'),

             age = input('请输入你的年龄：'))
# print(dict1)

print("我的名字是：{},性别：{},年龄：{},喜欢敲代码".format(dict1['name'],dict1['gender'],dict1['age']))

height = input('请输入您的身高：')

mobilephone = input('请输入您的联系方式：')
# ython 字典(Dictionary) update() 函数把字典dict2的键/值对更新到dict里。
# dict.update(dict2)
dict1.update({'height':height,'mobilephone':mobilephone})