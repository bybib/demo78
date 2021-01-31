"""1. 把字符串转成列表 - list()

2. 完成任意整数序列的相加 - 生成一个整数序列，里面全是数字。求里面所有数字的和

3. 定义函数：判断一个对象（列表，字典，字符串）的长度是否大于5，如果大于5，输出True；否则输出False。--if 判断嵌套"""
# 作业一
str1 = "adcd"
listl = list(str1)
print(listl)

# 作业二

num = int(input("请输入数字: "))
sum1 = 0
for i in range(num):
    sum1 += i
print(sum1)

# 作业三
# 首先定义一个函数
def object(object):
    if type(object) == list or type(object) == dict or type(object) == str:
        length1 = len(object)
        if length1 > 5:
            print("True")
        else:
            print("False")
    else:
        print("不符合数据类型")


object("(1,2,3,4)")
