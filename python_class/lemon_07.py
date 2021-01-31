# 定义函数
# args不定长参数   适用场景：不确定是否有参数，也不确定参数的个数
print("666")
print("44444")
def good_job(salary, bonus, subsidy=4000, *args,**kwargs):
    sum1 = salary + bonus + subsidy
    for num in args:
        sum1 += num
    # print(sum1)
    # print('参数kwargs为：{}'.format(kwargs))
    # 把**kwargs传入的参值与sum1相加求和 ，可以循环遍历
    for i in kwargs:
        # 取到i的值
        # print(kwargs.get(i))
        sum1 += kwargs.get(i)
        return sum1   #接收



    # print('参数args:{}'.format(args))
    # print('工资的总和是：{}'.format(sum1))
good_job(2000, 3000, 500, 6000,500,aa=100,bb=200)

# 扩展： ["hello","python","lemon"]   split
# 将一个字符串以一个符号截断,返回列表(str,num)   ----str字符串   num---截取的次数，默认-1截取到最后
str1 = "hello ,python,lemon"
str2 = str1.split(',')
print(str2)