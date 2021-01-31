# 作业
name = str(input("请输入姓名: "))
age = int(input("请输入年龄: "))
sex = str(input("请输入性别: "))
print('''******
 姓名：{}
 性别：{}
 年龄:{}
# ******'''.format(name, age, sex))



str1 = 'python hello aaa 123123aabb'
print(str1[:6:])
print('o a' in str1)
print('he' in str1)
print('ab' in str1)

print(str1.replace("python", "lemon"))
print(str1.index('aaa'))