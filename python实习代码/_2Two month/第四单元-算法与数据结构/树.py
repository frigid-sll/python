# # 二叉树节点的定义类
# class Node(object):
#
#     def __init__(self, item):
#         self.item = item
#         # 左孩子指向,新节点一般为叶子节点，叶子节点没有后续，所以设置为None
#         self.lchild = None
#         # 右孩子指向
#         self.rchild = None
#
#
# class Binary_tree(object):
#     """树类"""
#     def __init__(self):
#         # 定义出根节点 root
#         self.root = None
#
#     def add(self, item):
#         # 创建节点
#         new_node = Node(item)
#         # 判断树是否为空，如果是空树，则直接赋值给root，如果不为空，找到第一个为空的自孩子进行赋值
#         if not self.root:
#             # 如果为空，做相应处理
#             self.root = new_node
#         else:
#             # 创建储存节点的列表
#             queue = []
#             # 将根节点添加到节点列表中去
#             queue.append(self.root)
#             while len(queue) > 0:
#                 node = queue.pop(0)
#                 # 判断节点是否含有左孩子
#                 if node.lchild:
#                     queue.append(node.lchild)
#                 else:
#                     node.lchild = new_node
#                     break
#                 # 判断节点是否含有右孩子
#                 if node.rchild:
#                     queue.append(node.rchild)
#                 else:
#                     node.rchild = new_node
#                     break
#
#     def breadth_travel(self):
#         """广度优先遍历"""9
#         if self.root == None:  # 判断是否为空
#             return
#         else:
#             queue = []
#             queue.append(self.root)
#             while len(queue) > 0:
#                 # 从节点列表中获取一个节点
#                 node = queue.pop(0)
#
#                 print(node.item, end=' ')
#                 # 将节点的左孩子放入节点列表
#                 if node.lchild:
#                     queue.append(node.lchild)
#                 # 将节点的右孩子放入节点列表
#                 if node.rchild:
#                     queue.append(node.rchild)
#             print()
#
    # def preorder_travel(self, root):
    #     """深度优先遍历之先序遍历"""
    #     if root:  # 如果根节点存在
    #         print (root.item, end=" ")
    #         self.preorder_travel(root.lchild)
    #         self.preorder_travel(root.rchild)
#
#     def inorder_travel(self, root):
#         """深度优先遍历之中序遍历"""
#         if root:
#             self.inorder_travel(root.lchild)
#             print(root.item, end=" ")
#             self.inorder_travel(root.rchild)
#
#     def postorder_travel(self, root):
#         """深度优先遍历之后序遍历"""
#         if root:
#             self.postorder_travel(root.lchild)
#             self.postorder_travel(root.rchild)
#             print(root.item, end=" ")
#
# if __name__ == '__main__':
#     bt = Binary_tree()
#     bt.add(0)
#     bt.add(1)
#     bt.add(2)
#     bt.add(3)
#     bt.add(4)
#     bt.add(5)
#     bt.add(6)
#     bt.add(7)
#     bt.add(8)
#     bt.add(9)
#     bt.breadth_travel()
#     bt.preorder_travel(bt.root)  # 先序遍历
#     print()
#     bt.inorder_travel(bt.root)  # 中序遍历
#     print()
#     bt.postorder_travel(bt.root)  # 后序遍历


# class Node(object):
#     def __init__(self,item):
#         self.item=item
#         self.lchild=None
#         self.rchild=None
#
# class tree(object):
#     def __init__(self):
#         self.root=None
#
    # def add(self,item):
        # node=Node(item)
        # if self.root is None:
        #     self.root=node
        # else:
        #     list=[]
        #     list.append(self.root)
        #     while len(list)>0:
        #         son=list.pop(0)
        #         if son.lchild is None:
        #             son.lchild=node
        #             break
        #         else:
        #             list.append(son.lchild)
        #         if son.rchild is None:
        #             son.rchild=node
        #             break
        #         else:
        #             list.append(son.rchild)
#
    # def travel(self):
        # if self.root is None:
        #     return
        # else:
        #     list = []
        #     list.append(self.root)
        #     while len(list) > 0:
        #         son = list.pop(0)
        #         print(son.item, end=' ')
        #         if son.lchild is not None:
        #             list.append(son.lchild)
        #         if son.rchild is not None:
        #             list.append(son.rchild)
#
#     def first(self,x):
#         if x is None:
#             return
#         else:
#             print(x.item,end=' ')
#             self.first(x.lchild)
#             self.first(x.rchild)
#
#     def second(self,x):
#         if x is None:
#             return
#         else:
#             self.second(x.lchild)
#             print(x.item,end=' ')
#             self.second(x.rchild)
#
#     def last(self,n):
#         if n is None:
#             return
#         else:
#             self.last(n.lchild)
#             self.last(n.rchild)
#             print(n.item,end=' ')
#
#
# t=tree()
# t.add(0)
# t.add(1)
# t.add(2)
# t.add(3)
# t.add(4)
# t.add(5)
# t.add(6)
# t.add(7)
# t.add(8)
# t.add(9)
# t.travel()
# print()
# t.first(t.root)
# print()
# t.second(t.root)
# print()
# t.last(t.root)


class Node(object):
    def __init__(self,item):
        self.item=item
        self.lchild=None
        self.rchild=None

class shu(object):
    def __init__(self):
        self.root=None

    def add(self,item):
        node=Node(item)
        if self.root is None:
            self.root=node
        else:
            list=[]
            list.append(self.root)
            while len(list)>0:
                x=list.pop(0)
                if x.lchild is None:
                    x.lchild=node
                    break
                else:
                    list.append(x.lchild)
                if x.rchild is None:
                    x.rchild=node
                    break
                else:
                    list.append(x.rchild)

    def travel(self):
        if self.root is None:
            pass
        else:
            list = []
            list.append(self.root)
            while len(list)>0:
                x = list.pop(0)
                print(x.item)
                if x.lchild is not None:
                    list.append(x.lchild)
                if x.rchild is not None:
                    list.append(x.rchild)

    def xian(self,x):
        if x is None:
            pass
        else:
            print(x.item,end=' ')
            self.xian(x.lchild)
            self.xian(x.rchild)

s=shu()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(6)
s.add(7)
# s.travel()
s.xian(s.root)










