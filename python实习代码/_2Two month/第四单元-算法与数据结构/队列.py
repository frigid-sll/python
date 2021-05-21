"""
Queue() 创建一个空的队列
enqueue(item) 往队列中添加一个item元素
dequeue() 从队列头部删除一个元素
is_empty() 判断一个队列是否为空
size() 返回队列的大小
"""

# class Queue(object):
#     """创建一个队列"""
#     def __init__(self):
#         self.item = []
#
#     def enqueue(self, item):
#         '''往队列中添加一个item元素'''
#         self.item.append(item)
#
#     def dequeue(self):
#         '''从队列头部删除一个元素'''
#         return self.item.pop(0)
#
#     def is_empty(self):
#         '''判断一个队列是否为空'''
#         return self.item == []
#
#     def size(self):
#         '''返回队列的大小'''
#         return len(self.item)
#
#
# if __name__ == '__main__':
#     queue = Queue()
#     print(queue.is_empty())
#     print(queue.size())
#     queue.enqueue(1)
#     queue.enqueue(2)
#     queue.enqueue(3)
#     queue.enqueue(4)
#     print(queue.is_empty())
#     print(queue.size())
#     print(queue.dequeue())
#     print(queue.dequeue())
#     print(queue.dequeue())
#     print(queue.dequeue())
#     print(queue.is_empty())
#     print(queue.size())


"""
Queue() 创建一个空的队列
enqueue(item) 往队列中添加一个item元素
dequeue() 从队列头部删除一个元素
is_empty() 判断一个队列是否为空
size() 返回队列的大小
"""



class Queue(object):
    def __init__(self):
        self.queue=[]

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop()

    def is_empty(self):
        if len(self.queue)==0:
            return True
        else:
            return False

    def size(self):
        return len(self.queue)




# class Queue(object):
#     def __init__(self):
#         self.queue=[]
#
#     def is_empty(self):
#         return self.queue == []
#
#     def enqueue(self,item):
#         return self.queue.append(item)
#
#     def dequeue(self):
#         return self.queue.pop(0)
#
#     def size(self):
#         return len(self.queue)
#
# queue=Queue()
# print(queue.is_empty())
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)
# print(queue.size())
# print(queue.dequeue())
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# print(queue.is_empty())





















# class Queue(object):
#     """创建一个空的队列"""
#     def __init__(self):
#         self.queue = []
#
#     def enqueue(self,item):
#         """往队列中添加一个item元素"""
#         return self.queue.append(item)
#
#     def dequeue(self):
#         """从队列头部删除一个元素"""
#         return self.queue.pop(0)
#
#     def is_empty(self):
#         """判断一个队列是否为空"""
#         return self.queue == []
# 
#     def size(self):
#         """返回队列的大小"""
#         return len(self.queue)
#
# if __name__ == '__main__':
#     queue = Queue()
#     print(queue.is_empty())
#     print(queue.size())
#     queue.enqueue(1)
#     queue.enqueue(2)
#     queue.enqueue(3)
#     queue.enqueue(4)
#     print(queue.size())
#     print(queue.dequeue())
#     print(queue.dequeue())
#     print(queue.dequeue())
#     print(queue.dequeue())
