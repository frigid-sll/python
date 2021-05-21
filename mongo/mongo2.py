# from  pymongo import MongoClient
# c=MongoClient(host="localhost",port=27017)
# m=c["text"]["mm"]
# m.insert_manyny([{"name":"小明","age":18},{"name":"小花","age":19}])
# m.insert_one({"name":"小鱼","age":20})
# s=m.find_one({"name":"小明"})
# print(s)
# ss=m.find({"name":"小黄"},{'_id':0,'age':0})
# for i in ss:
#     print(i)
# m.update({"name":"小花"},{'$set':{"name":"小黄"}},multi=True)
# m.delete_one({'name':'小黄'})

n=m.aggregate([{'$match':{'age':{'$gt':10}}},{'$sort':{'age':1}}])
for i in n:
    print(i)

