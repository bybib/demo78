# 作业1
a = [1, 2, '6', 'summer']
if "i" in a:
    print("存在")
else:
    print("不存在")
# 作业二
dict_1 = {"class_id": 45, "num": 20}
# dict_2 = dict_1.get("num")
dict_2 = dict_1["num"]
# print(dict_2)
if dict_2 > 5:
    print("班级的人数为:{}".format(dict_2))
else:
    print("班级人数少于5人")

# 作业三

list1 = ['肥兔', '鹿鹿', '耳洞', '蓝山', '柠檬']
# 方法一  手动扩充
# dict1 = {"name": "肥兔", "gender": "male", "age": "18", "city": "湖南"}
# dict2 = {"name": "鹿鹿", "gender": "male", "age": "19", "city": "江苏"}
# dict3 = {"name": "耳洞", "gender": "male", "age": "20", "city": "郑州"}
# dict4 = {"name": "蓝山", "gender": "male", "age": "21", "city": "北京"}
# dict5 = {"name": "柠檬", "gender": "male", "age": "22", "city": "上海"}
# list2 = [dict1, dict2, dict3, dict4, dict5]
# print(list2)

# 方法二
# 定义一个列表存新数据
list2 = []
for name1 in list1:
    dict_1 = dict(name=name1, gender="male", age=18, city="上海")
    list2.append(dict_1)  # 括号里面是追加的元素
print(list2)





