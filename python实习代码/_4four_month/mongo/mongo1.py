# from pymongo import MongoClient
# client=MongoClient(host='localhost',port=27017)
# collection=client['test']['py']

#单条插入
# collection.insert_one({'name':'zhangsan','age':20})
#多条插入
# collection.insert_many([{'name':'lisi','age':30},{'name':'wangwu','age':10}])
#输出查询结果  是个生成器
# ret=collection.find()
# for x in ret:
#     print(x)

# item_list=[{'name':'test1000{}'.format(i)} for i in range(1,10)]
# # print(item_list)
# collection.insert_many(item_list)

# ret= collection.find()
# for x in ret:
#     print(x)

# collection.delete_one({'age':100})

# collection.update({'name':'test'},{'age':220})


# from pymongo import MongoClient
# class Mongo:
#     def __init__(self):
#         client=MongoClient(host='localhost',port=27017)
#         self.collection=client['test']['students']
#
#     def insert_one_test(self):
#         self.collection.insert_one({'name':'xiaohong','age':19})
#
# mongo=Mongo()
# mongo.insert_one_test()

# from pymongo import MongoClient
# client=MongoClient(host='localhost',port=27017)
# collection=client['test']['students']
# ret=collection.aggregate([{"$group":{'_id':'$age'}}])
# for x in ret:
#     print(x)
# ret=collection.find({'$or':[{'age':{'$gt':20}},{'age':{'$lt':17}}]})
# for x in ret:
#     print(x)
# collection.delete_one({'age':16})

from pymongo import MongoClient
client=MongoClient(host='localhost',port=27017)
collection=client['test']['students']
# ret= collection.aggregate([{'$group':{'_id':'$gender'}}])
# for x in ret:
#     print(x)
ret=collection.find({'$or':[{'age':{'$gt':20}},{'age':{'$lt':15}}]})
for x in ret:
    print(x)



