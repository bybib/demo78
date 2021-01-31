# 从python_class这个包中导入lemon_10这个文件
from python_class import lemon_10
# 获取到这个表单
# ***************这部分又可以封装成函数，提高代码的复用性
def execute_fun(filename,sheetname):
    cases = lemon_10.read_data(filename, sheetname)
    print(cases)
    # 目的是从用例中取出数据，然后一个个发送接口请求  ，这里用到for循环
    for case in cases:
        # print(case)
    #把case 中的数据一条一条取出来
        case_id = case.get('case_id')
        url = case.get("url")   # 取出接口的 url
        data = case.get("data")  #取出参数     注意：此处data的数据是从文本中取出来的类型是字符串，不是字典
        # eval()函数是从字符串里面获取到python表达式
        data = eval(data)   # 从字符串中获取python表达式
        # print(type(data))
        expected = case.get("expected")   #取出预期结果
        expected = eval(expected)   # 注意:从文本中取出的字符串类型 要用eval()函数获取python表达式
        expected_msg = expected.get("msg")
        print('真实执行结果:{}'.format(expected_msg))
        # print(url, data, expected)
        # 1.取出数据像接口发送请求 2.调用接口发送的参数(有返回值)
        rel_result = lemon_10.api_func(url_api=url,data_api=data)
        # print(rel_result)
        # 取出实际的结果
        rel_msg = rel_result.get("msg")
        print('实际执行结果：{}'.format(rel_msg))

        # 用 if做判断 ，如果预期结果和实际结果相等，则用例通过
        if expected_msg == rel_msg:
            final_result = "Passed"   # 定义一个最终结果
            print("第：{}执行用例通过！".format(case_id))
        else:
            final_result = "Failed"
            print("第{}条执行用例不通过！".format(case_id))
        print('@'*20)

        # 把读取的结果写入表单
        # 调用自定义写的函数
        lemon_10.write_result(filename, sheetname, final_result, case_id+1, 8)  # 调用写入结果函数
execute_fun("test_case_api.xlsx","register")




