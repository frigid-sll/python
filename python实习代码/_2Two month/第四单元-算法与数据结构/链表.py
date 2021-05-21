# 单向链表


# 创建单链表节点类
# class Node(object):
#     """创建单链表节点类"""
#     def __init__(self, item):
#         """创建单链表节点"""
#         self.item = item   # 元素域
#         self.next = None   # 下一个节点的链接域
#
# class SingleLinkList(object):
#     """创建单向链表类"""
#     def __init__(self):
#         self.__head = None   # 头结点self.__head
#
#     def is_empty(self):
#         '''链表是否为空'''
#         # 通过判断头结点是否为None
#         return self.__head is None
#
#     def length(self):
#         '''链表长度'''
#         if self.is_empty():
#             return 0
#         else:
#             # 创建计数器
#             count = 0
#             # 创建一个游标，指向头结点
#             cur = self.__head
#             # 移动游标做统计
#             while cur is not None:
#                 count += 1
#                 # 移动游标
#                 cur = cur.next
#             return count
#
#     def travel(self):
#         '''遍历整个链表'''
#         # 创建一个游标，指向头结点
#         cur = self.__head
#         # 当游标指向位置不为空时
#         while cur is not None:
#             print(cur.item, end=" ")
#             # 移动游标
#             cur = cur.next
#         print()  # print（） 自带换行功能
#
#     def add(self, item):
#         '''链表头部添加元素'''
#
#         # 创建新节点对象，将数据存储到新节点中
#         node = Node(item)
#         # 判断链表是否为空
#         if self.is_empty():
#             # 头部添加--将头结点指向node节点
#             self.__head = node
#         else:
#             # 将新节点的next指向旧头结点
#             node.next = self.__head
#             # 将头结点指向新的头结点
#             self.__head = node
#
#     def append(self, item):
#         '''链表尾部添加元素'''
#         # 创建新节点对象，将数据存储到新节点中
#         node = Node(item)
#         # 判断链表是否为空
#         if self.is_empty():
#             # 头部添加--将头结点指向node节点
#             self.__head = node
#         else:
#             # 创建出cur游标，找到尾节点
#             cur = self.__head
#             # 移动游标，游标指向位置不为空时
#             while cur.next is not None:
#                 # 移动游标
#                 cur = cur.next
#             # 当循环结束之后，cur指向尾节点，此时将新的尾节点添加到旧的尾节点之后
#             cur.next = node
#
#     def insert(self, pos, item):
#         '''指定位置添加元素'''
#         if pos <= 0:
#             self.add(item)
#         elif pos >= self.length() - 1:
#             self.append(item)
#         else:
#             # 创建新节点
#             node = Node(item)
#
#             # 创建计数器
#             count = 0
#
#             # 创建游标
#             cur = self.__head
#
#             while count < pos - 1:
#                 count += 1
#                 cur = cur.next
#
#             # 将新节点添加到链表中，新节点指向后续节点
#             node.next = cur.next
#             # 前节点指向新节点
#             cur.next = node
#
#     def remove(self,item):
#         '''删除节点'''
#         if self.is_empty():
#             return
#         else:
#             cur = self.__head
#             # 设置前驱游标，默认为None
#             pre = None
#             while cur is not None:
#                 if cur.item == item:
#                     # 要删除的节点为头结点
#                     if cur == self.__head:
#                         self.__head = cur.next
#                     else:
#                         # 待删除节点在链表中部和尾部的时候
#                         pre.next = cur.next
#                     break
#                 else:
#                     # 修改前驱指向，记录当前位置
#                     pre = cur
#                     cur = cur.next
#
#     def search(self,item):
#         '''查找节点是否存在'''
#         # 创建遍历游标
#         cur = self.__head
#
#         while cur is not None:
#             if cur.item == item:
#                 return True
#             else:
#                 cur = cur.next
#         return False
#
#
# if __name__ == '__main__':
#     sll = SingleLinkList()
#     print(sll.is_empty())
#     print(sll.length())
#     # sll.travel()
#     sll.add(1)
#     sll.add(2)
#     sll.add(3)
#     sll.add(4)
#     sll.travel()
#     sll.append(1)
#     sll.append(2)
#     sll.append(3)
#     sll.append(4)
#     sll.travel()
#     sll.insert(-100,66)
#     sll.travel()
#     sll.insert(5, 66)
#     sll.travel()
    # sll.insert(100, 66)
    # sll.travel()
    # sll.remove(66)
    # sll.travel()
    # sll.remove(66)
    # sll.travel()
    # sll.remove(66)
    # sll.travel()
    # print(sll.search(100))
    # print(sll.search(1))


# class Node(object):
#     def __init__(self,item):
#         self.item=item
#         self.next=None
#
# class biao(object):
#     def __init__(self):
#         self.head=None
#
#     def is_empty(self):
#         return self.head is None
#
#     def travel(self):
#         cur=self.head
#         while cur is not None:
#             print(cur.item)
#             cur=cur.next
#
#     def length(self):
#         count=0
#         cur=self.head
#         while cur is not None:
#             count+=1
#             cur=cur.next
#         return count
#
#     def tou(self,n):
#         node=Node(n)
#         if self.is_empty():
#             self.head=node
#         else:
#             node.next=self.head
#             self.head=node
#
#     def wei(self,n):
#         node=Node(n)
#         if self.is_empty():
#             self.head=node
#         else:
#             cur=self.head
#             while cur.next is not None:
#                 cur=cur.next
#             cur.next=node
#
#     def insert(self,pos,item):
#         if pos<=0:
#             self.tou(item)
#         elif pos>=self.length()-1:
#             self.wei(item)
#         else:
#             cur=self.head
#             count=0
#             node=Node(item)
#             while cur is not None:
#                 if count==pos-1:
#                     node.next=cur.next
#                     cur.next=node
#                     break
#                 count+=1
#                 cur=cur.next
#
#     def remove(self,n):
#         pre=None
#         count=0
#         cur=self.head
#         while cur is not None:
#             if n==count:
#                 if n == 0:
#                     self.head = cur.next
#                 elif n == self.length() - 1:
#                     pre.next = None
#                 else:
#                     pre.next=cur.next
#                 break
#             else:
#                 pre=cur
#                 cur=cur.next
#
#     def search(self,item):
#         cur=self.head
#         while cur is not None:
#             if cur.item==item:
#                 return True
#             else:
#                 cur=cur.next
#         return False
#
#
#
#
# l=biao()
# l.tou(1)
# l.tou(2)
# l.tou(3)
# l.wei(4)
# l.insert(66,6)
# print(l.search(6))
# l.remove(0)
# l.travel()



# class Node(object):
#     def __init__(self,item):
#         self.item=item
#         self.next=None
#
# class biao(object):
#     def __init__(self):
#         self.head=None
#
#     def is_empty(self):
#         if self.head==None:
#             return True
#         else:
#             return False
#
#     def length(self):
#         count=0
#         cur=self.head
#         while cur is not None:
#             count+=1
#             cur=cur.next
#         return count
#
#     def travel(self):
#         cur = self.head
#         while cur is not None:
#             print(cur.item,end=' ')
#             cur=cur.next
#
#     def add(self,item):
#         node=Node(item)
#         if self.head is None:
#             self.head=node
#         else:
#             node.next=self.head
#             self.head=node
#
#     def append(self,item):
#         node=Node(item)
#         if self.head is None:
#             self.head=node
#         else:
#             cur=self.head
#             while cur.next is not None:
#                 cur=cur.next
#             cur.next=node
#
#     def insert(self,pos,item):
#         if pos<=0:
#             self.add(item)
#         elif pos>=self.length()-1:
#             self.append(item)
#         else:
#             node=Node(item)
#             count=0
#             cur=self.head
#             pre=None
#             while cur is not None:
#                 if count==pos:
#                     pre.next=node
#                     node.next=cur
#                 else:
#                     pre=cur
#                     cur=cur.next
#                 count+=1
#
#     def remove(self,n):
#         cur=self.head
#         if self.is_empty():
#             return
#         else:
#             count=0
#             pre=None
#             while cur is not None:
#                 if n==count:
#                     if n == 0:
#                         self.head = cur.next
#                     elif n == self.length() - 1:
#                         pre.next = None
#                     else:
#                         pre.next = cur.next
#                 else:
#                     pre = cur
#                     cur = cur.next
#                 count+=1
#
#     def search(self,item):
#         cur=self.head
#         while cur is not None:
#             if item==cur.item:
#                 return True
#             else:
#                 cur=cur.next
#         return False
#
#
# l=biao()
# l.add(1)
# l.add(2)
# l.append(3)
# l.insert(1,0)
# l.remove(0)
# print(l.search(6))
# l.travel()


# class Node(object):
#     def __init__(self,item):
#         self.item=item
#         self.next=None
#
# class lian(object):
#     def __init__(self):
#         self.head=None
#
#     def is_empty(self):
#         return self.head is None
#
#     def length(self):
#         count=0
#         cur=self.head
#         while cur is not None:
#             count+=1
#             cur=cur.next
#         return count
#
#     def travel(self):
#         cur=self.head
#         while cur is not None:
#             print(cur.item)
#             cur=cur.next
#
#     def add(self,item):
#         node=Node(item)
#         node.next=self.head
#         self.head=node
#
#     def append(self,item):
#         node=Node(item)
#         cur=self.head
#         while cur.next is not None:
#             cur=cur.next
#         cur.next=node
#
#     def insert(self,pos,item):
#         node=Node(item)
#         if pos<=0:
#             self.add(item)
#         elif pos>=self.length():
#             self.append(item)
#         else:
#             count=0
#             node=Node(item)
#             pre=None
#             cur=self.head
#             while cur is not None:
#                 if pos==count:
#                     pre.next=node
#                     node.next=cur
#                 else:
#                     pre=cur
#                     cur=cur.next
#                 count+=1
#
#     def gai(self,pos,item):
#         node=Node(item)
#         count=0
#         pre=None
#         cur=self.head
#         if self.is_empty():
#             return
#         else:
#             if pos <= 0:
#                 self.head=node
#                 node.next = cur.next
#             else:
#                 while cur is not None:
#                     if pos == count:
#                         pre.next = node
#                         node.next = cur.next
#                     else:
#                         pre = cur
#                         cur = cur.next
#                     count += 1
#
#     def remove(self,pos):
#         if self.is_empty():
#             return
#         else:
#             cur=self.head
#             count=0
#             pre=None
#             if pos<=0:
#                 self.head=cur.next
#             else:
#                 while cur is not None:
#                     if pos==count:
#                         pre.next=cur.next
#                     else:
#                         pre=cur
#                         cur=cur.next
#                     count+=1
#
#     def search(self,item):
#         if self.is_empty():
#             return False
#         else:
#             cur=self.head
#             while cur is not None:
#                 if item==cur.item:
#                     return True
#                 cur=cur.next
#             return False
#
# b=lian()
# b.add(1)
# b.add(2)
# b.append(3)
# b.insert(2,5)
# b.gai(1,8)
# b.remove(1)
# b.remove(2)
# print(b.search(2))
# b.travel()
# b.length()






class Node(object):
    def __init__(self,item):
        self.item=item
        self.next=None

class l(object):
    def __init__(self):
        self.head=None

    def length(self):
        if self.head==None:
            return 0
        else:
            count=0
            cur=self.head
            while cur is not None:
                count+=1
                cur=cur.next
            return count

    def travel(self):
        cur = self.head
        while cur is not None:
            print(cur.item)
            cur = cur.next

    def add(self,item):
        node=Node(item)
        if self.head is None:
            self.head=node
        else:
            node.next=self.head
            self.head=node

    def append(self,item):
        node=Node(item)
        if self.head is None:
            self.head=node
        else:
            cur=self.head
            while cur.next is not None:
                cur=cur.next
            cur.next=node

    def insert(self,pos,item):
        node=Node(item)
        count=0
        pre=None
        cur=self.head
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            while cur is not None:
                if pos == count:
                    pre.next = node
                    node.next = cur
                count += 1
                pre = cur
                cur = cur.next

    def gai(self,pos,item):
        node=Node(item)
        cur=self.head
        pre=None
        count=0
        if pos==0:
            cur=cur.next
            node.next=cur
            self.head=node
        elif pos==self.length()-1:
            while cur.next is not None:
                pre=cur
                cur=cur.next
            pre.next=node
        else:
            while cur.next is not None:
                if count==pos:
                    pre.next=node
                    node.next=cur.next
                count+=1
                pre=cur
                cur=cur.next


f=l()
# print(f.length())
f.add(1)
f.add(2)
f.append(3)
# print(f.length())
f.insert(2,6)
f.gai(1,9)
f.travel()


