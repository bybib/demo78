# 占位符{}或%  %s代表字符串（万能） %d代表数字  %f代表小数
# name="yang"
# gender="male"
# hobby="篮球"
# print('''
# ----{}的基本信息----
# name：{}
# gender:{}
# hobby:{}
# '''.format(name,name,gender,hobby))

name = "yang"
gender = "male"
hobby = "篮球"
age = 18
price = 16.5
print('''
----%s的基本信息----
name：%s
gender:%s
hobby:%s
age:%d
price:%s
''' % (name, name, gender, hobby, age, price))