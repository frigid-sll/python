#json数据格式：
# {}：代表对象
# []:代表数组
# "":key和value
# ：断开key和value

#json四个函数
# json.loads():把jsonstr转python类型（dict)
# json.load():吧文件转python类型（dict)
# json.dumps():吧python类型（dict)转成jsonstr
# json.dump():吧python类型（dict)转为文件


# import json
# contentJson='{"name":"zhangsan","age":25}'
# print(contentJson)
# jsonA=json.loads(contentJson)
# print(type(jsonA))
# print(jsonA)
# jsonB=json.dumps(jsonA)
# print(jsonB)


# import os
# os.rename('json.py','_03json.py')

# import json
# contentJson='{"name":"张三","age":25}'
# print(type(contentJson))
# jsonA=json.loads(contentJson)
# print(jsonA)
# jsonB=json.dumps(jsonA)
# print(jsonB)

#将python类型写入文件
# jsonA={'name':'张三','age':25}
# import json
# with open('student.json',mode='w') as f:
#     json.dump(jsonA,f,ensure_ascii=False)    #ensure_ascii=False不让汉文转为ASCII
#     #f.write(jsonA)      #不允许用普通文件的方式写入dict
#
# #将json文件转为python类型
# with open('student.json',mode='r') as f:
#     contentJson=json.load(f)
#     print(contentJson)
#     print(type(contentJson))

import json
# contentJson='{"name":"张三","age":29}'
# print(type(contentJson))
# jsonA=json.loads(contentJson)
# print(jsonA)
# print(type(jsonA))
# jsonB=json.dumps(jsonA)
# print(jsonB)
# print(type(jsonB))
# with open('student2.json',mode='w') as f:
#     json.dump(jsonA,f,ensure_ascii=False)

# with open('student2.json',mode='r') as f:
#     s=json.load(f)
#     print(s)



# import json
# contentJson='{"name":"张三","age":25}'
# print(type(contentJson))
# print(contentJson)
# jsonA=json.loads(contentJson)
# print(jsonA)
# print(type(jsonA))
# jsonB=json.dumps(jsonA,ensure_ascii=False)
# print(jsonB)
# with open('student3.json',mode='w') as f:
#     json.dump(jsonA,f,ensure_ascii=False)
# with open('student3.json',mode='r') as f:
#     r=json.load(f)
#     print(r)






# import json
# a='{"name":"zhangsan","age":25}'
# print(type(a))
# b=json.loads(a)
# print(type(b))
# with open('a.txt',mode='w') as f:
#     json.dump(b,f)

