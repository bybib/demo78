# 列表
# list   列表的元素可以被改变：增加，删除，修改
# 1.增加
# list1 = [20, 3.14, True, [1, 2, 3, 4]]
# print(list1)
# list1.append('柠檬')
# print(list1)
# list1.insert(2,'蜗牛')
# print(list1)

# 删除
# 1.默认删除最后一个元素
# 2.
# 1.可以指定元素的索引进行删除(pop)
# 2.指定元素本身进行删除(remove)
# list1.pop(1)
# print(list1)
# list1.remove(3.14)
# print(list1)

# 修改  进行重新赋值
# list1[1] = 666
# print(list1)
# 元组   元组中的元素不能被改变
# tuple1 = (20, 3.14, True, "lemon")
# print(tuple1)
# 改变元组中的元素
# list1 = list(tuple1)
# print(list1)
# list1[3] ="python"
# print(list1)
# tuple2 = tuple(list1)
# print(tuple2)

# 字典
dict1 = {"name": "lemon", "age": 22, "hobby": "篮球"}
# 1.通过键来取
# print(dict1["age"])
# 2.通过.get()来取值
# print(dict1.get("age"))

# 增加  如果key不存在，新增加一个键值对
# dict1["sex"] = "女"
# print(dict1)
# 2.如果key值存在，更新一个键值对的value值
# dict1["hobby"] = "football"
# print(dict1)

# 删除  指定key进行删除
# dict1.pop("name")
# print(dict1)


# 增加多个元素
# dict1.update({"city": "上海","weight": "175"})
# print(dict1)


# 控制流   if判断  for循环
# if 条件:   # 条件成立进入下一步
#     子代码(执行语句)
# elif 条件: 条件成立进入下一步    # elif可以有多个，也可以没有
#      子代码(执行语句)
#
# else:  #没有条件
#       子代码(执行语句)

# if 判断
# money = int(input("请输入金额: ")) # input输出的是字符串  用int转换整形
# if money >= 200:
#     print("买房子")
# elif money > 100:
#     print("买辆车")
# elif money > 50:
#     print("买手机")
# else:
#     print("打工人，加油")

# for循环
# count = 0  # 变量初始化等于0
# str1 = "我爱python!"
# for i in str1:   # 缩进里面是for的循环体
#     print(i)
#     print("*" * 20)
#     count += 1
# print(len(str1))
# print(count)

# list1 = ["titi", "柠檬", "fafa", "耳东"]
# for name in list1:
#     if name == "fafa":
#         # break # 中断提跳出整个循环
#         continue # 继续跳出本次循环
#     print(name)

# range 与for一块使用
for num in range(0, 10, 2):   # stop取头不取尾
    print(num)