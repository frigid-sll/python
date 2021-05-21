
"""栈（也称下压栈，堆栈）是仅允许在表尾进行插入和删除操作的线性表。

我们把允许插入和删除的一端称为栈顶（top），另一端称为栈底（bottom）。

栈是一种后进先出（Last In First Out）的线性表，简称（LIFO)结构。
"""

# class Stack(object):
#     """栈类"""
#     def __init__(self):
#         self.stack = []
#
#     def push(self, item):
#         '''添加一个新的元素item到栈顶'''
#         self.stack.append(item)
#
#     def pop(self):
#         '''弹出栈顶元素'''
#         return self.stack.pop()
#
#     def peek(self):
#         '''返回栈顶元素'''
#         print(self.stack[self.size()-1])
#
#     def is_empty(self):
#         '''判断栈是否为空'''
#         return self.stack == []
#
#     def size(self):
#         '''返回栈的元素个数'''
#         return len(self.stack)
#
# if __name__ == '__main__':
#     stack = Stack()
#     stack.push(1)
#     stack.push(2)
#     stack.push(3)
#     # stack.peek()
#     # print(stack.size())
#     print(stack.pop())
#     print(stack.pop())
#     print(stack.pop())



"""
Stack() 创建一个新的空栈
push(item) 添加一个新的元素item到栈顶
pop() 弹出栈顶元素
peek() 返回栈顶元素
is_empty() 判断栈是否为空
size() 返回栈的元素个数
"""

# class Stack(object):
#     """创建一个新的空栈"""
#     def __init__(self):
#         self.stack = []
#
#     def push(self,item):
#         """添加一个新的元素item到栈顶"""
#         self.stack.append(item)
#
#     def pop(self):
#         """弹出栈顶元素"""
#         return self.stack.pop()

#     def peek(self):
#         """返回栈顶元素"""
#         return self.stack[self.size()-1]
#
#     def is_empty(self):
#         """判断栈是否为空"""
#         return self.stack == []
#
#     def size(self):
#         """返回栈的元素个数"""
#         return len(self.stack)

# if __name__ == '__main__':
#     stack = Stack()
#     print(stack.is_empty())
#     print(stack.size())
#     stack.push(1)
#     stack.push(2)
#     stack.push(3)
#     stack.push(4)
#     print(stack.peek())
#     print(stack.pop())
#     print(stack.peek())













"""
Stack() 创建一个新的空栈
push(item) 添加一个新的元素item到栈顶
pop() 弹出栈顶元素
peek() 返回栈顶元素
is_empty() 判断栈是否为空
size() 返回栈的元素个数
"""








# class Stack(object):   # 后进先出
#     """创建一个新的空栈"""
#     def __init__(self):
#         self.stack = []
#
#     def push(self,item):
#         """添加一个新的元素item到栈顶"""
#         return self.stack.append(item)
#
#     def pop(self):
#         """弹出栈顶元素"""
#         return self.stack.pop()
#
#     def peek(self):
#         """返回栈顶元素"""
#         return self.stack[self.size()-1]
#
#     def is_empty(self):
#         """判断栈是否为空"""
#         return self.stack == []
#
#     def size(self):
#         """返回栈的元素个数"""
#         return len(self.stack)



stack = Stack()
print(stack.is_empty())
print(stack.size())
print("*"*20)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.size())
print("*"*20)
print(stack.peek())
print(stack.pop())
print(stack.peek())



