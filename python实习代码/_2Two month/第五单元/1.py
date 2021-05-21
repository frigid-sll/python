# from socket import *
#
# # 1. 创建udp套接字
# udp_socket = socket(AF_INET, SOCK_DGRAM)
# # 2. 准备接收方的地址
# dest_addr = ('192.168.43.85', 8080)
# # 3. 从键盘获取数据
# send_data = input("请输入要发送的数据:")
#
# # 4. 发送数据到指定的电脑上
# udp_socket.sendto(send_data.encode('gb2312'), dest_addr)
#
# # 5. 等待接收对方发送的数据
# recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
#
# # 6. 显示对方发送的数据
# # 接收到的数据recv_data是一个元组
# # 第1个元素是对方发送的数据 # 第2个元素是对方的ip和端口
# print(recv_data[0].decode('gb2312'))
# print(recv_data[1])
#
# # 7. 关闭套接字
# udp_socket.close()


# def q(**kwargs):
#     for x in kwargs.values():
#         print(x)
# q(m=1,n=2,s=3)

# import copy
# a=[[1,2],1,2]
# b=copy.deepcopy(a)
# print(id(a[0]),id(b[0]))

# def add(x, y, f):
#     return f(x) + f(y)
#
#
# print(add(-5, 6, abs))
# a=range(10)
# print(a)
# for x in a:
#     print(x)

# a=list(filter(lambda x:x%3,[1,2,3,4]))
# print(a)


# import timeit
# def a():
#     print(5)
# if __name__ == '__main__':
#     f1 = timeit.Timer('a()', 'from __main__ import a')
#     f=f1.timeit(10)
#     print(f)

# import timeit
# def a():
#     print(2)
# if __name__ == '__main__':
#     f=timeit.Timer('a()','from __main__ import a')
#     s=f.timeit(10)
#     print(s)

