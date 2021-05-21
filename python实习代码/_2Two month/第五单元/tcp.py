# from socket import *
# tcp_socket=socket(AF_INET,SOCK_STREAM)
# addr=('192.168.1.6',8080)
# tcp_socket.connect(addr)
# data=input("请输入你要发送的内容：")
# tcp_socket.send(data.encode('gbk'))
# recv_from=tcp_socket.recv(1024)
# print(recv_from.decode('gbk'))
# tcp_socket.close()

# from socket import *
# #
# # 创建socket
# tcp_client_socket = socket(AF_INET, SOCK_STREAM)
#
# # 目的信息
# server_addr = ('192.168.1.6', 8080)
# # 链接服务器
# tcp_client_socket.connect(server_addr)
#
# # 提示用户输入数据
# send_data = input("请输入要发送的数据：")
#
# tcp_client_socket.send(send_data.encode("gbk"))
#
# # 接收对方发送过来的数据，最大接收1024个字节
# recvData = tcp_client_socket.recv(1024)
# print('接收到的数据为:', recvData.decode('gbk'))
#
# # 关闭套接字
# tcp_client_socket.close()

#
# from socket import *
#
# # 创建socket
# tcp_server_socket = socket(AF_INET, SOCK_STREAM)
# # 本地信息
# address = ('', 7788)
# # 绑定
# tcp_server_socket.bind(address)
# # 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，这样就可以接收别人的链接了
# tcp_server_socket.listen(128)
#
# # 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
# # client_socket用来为这个客户端服务
# # tcp_server_socket就可以省下来专门等待其他新客户端的链接
# client_socket, clientAddr = tcp_server_socket.accept()
# # 接收对方发送过来的数据
# recv_data = client_socket.recv(1024)  # 接收1024个字节
# print('接收到的数据为:', recv_data.decode('gbk'))
# # 发送一些数据到客户端
# client_socket.send("thank you !".encode('gbk'))
# # 关闭为这个客户端服务的套接字，只要关闭了，就意味着为不能再为这个客户端服务了，如果还需要服务，只能再次重新连接
# client_socket.close()

# from socket import *
# tcp_socket=socket(AF_INET,SOCK_STREAM)
# addr=('192.168.1.6',8080)
# tcp_socket.connect(addr)
# data=input('请输入你要发送的内容：')
# tcp_socket.send(data.encode('gbk'))
# recv_from=tcp_socket.recv(1024)
# print(recv_from.decode('gbk'))
# tcp_socket.close()

# while True:
#     from socket import *
#     tcp = socket(AF_INET, SOCK_STREAM)
#     addr = ('', 8080)
#     tcp.bind(addr)


#     tcp.listen(100)
#     tcp2, tcp_ip = tcp.accept()
#     data = input('请输入你要向服务端发送的信息：')
#     tcp2.send(data.encode('gbk'))
#     recv_from = tcp2.recv(2014)
#     print('服务器为你的消息为：%s' % recv_from.decode('gbk'))
#     tcp2.close()
#     tcp.close()


# while True:
#     from socket import *
#     tcp = socket(AF_INET, SOCK_STREAM)
#     addr = ('192.168.1.6', 8080)
#     tcp.connect(addr)
#     data = input('请输入你要发送的内容：')
#     tcp.send(data.encode('gbk'))
#     recv_from = tcp.recv(1024)
#     print('收到的内容为：%s' % recv_from.decode('gbk'))
#     tcp.close()

# from socket import *
# tcp_1=socket(AF_INET,SOCK_STREAM)
# addr=('',8080)
# tcp_1.bind(addr)
# tcp_1.listen(100)
# q,w=tcp_1.accept()
# recv=q.recv(1024)
# print(recv.decode('gbk'))
# q.send('thankyou'.encode('gbk'))
# print(w)
# q.close()



# from socket import *`
# tcp_socket=socket(AF_INET,SOCK_STREAM)
# addr=('192.168.1.1',8080)
# tcp_socket.connect(addr)
# data=input('请输入你要发送的内容：')
# tcp_socket.send(data.encode('gbk'))
# recv_from=tcp_socket.recv(1024)
# print(recv_from.decode('gbk'))
# tcp_socket.close()

# a=[1,2,3,4,5]
#
#
# def cha(a,i):
#     first=0
#     last=len(a)-1
#     while first<=last:
#         x=(last+first)//2
#         if a[x]==i:
#             return True
#         elif i>a[x]:
#             first=x+1
#         else:
#             last=x-1
#     else:
#         return False
# def cha(a,i):
#     if len(a)==0:
#         return False
#     else:
#         x=len(a)//2
#         if a[x]==i:
#             return True
#         elif i>a[x]:
#             return cha(a[x+1:],i)
#         else:
#             return cha(a[:x],i)
# print(cha(a,5))


# from socket import *
# tcp=socket(AF_INET,SOCK_STREAM)
# addr=('',8080)
# tcp.bind(addr)
# tcp.listen(100)
# kehu,kehu_ip=tcp.accept()
# recv_data=kehu.recv(1024)
# print('收到客户端的信息为：%s'%recv_data.decode('gbk'))
# kehu.send('thankyou'.encode('gbk'))
# recv_data2=kehu.recv(1024)
# print(recv_data2.decode('gbk'))
# print(kehu_ip)
# kehu.close()
# tcp.close()





# from socket import *
# tcp_server_socket=socket(AF_INET,SOCK_STREAM)
# addr=('',7788)
# tcp_server_socket.bind(addr)
# tcp_server_socket.listen(100)
# tcp_client_socket,client_addr=tcp_server_socket.accept()
# data=input("请输入你要想服务端发送的信息：")
# tcp_client_socket.send(data.encode('gbk'))
# # data2=input('请输入你要回复客户端的信息：')
# rec=tcp_client_socket.recv(2014)
# print(rec.decode('gbk'))
# tcp_client_socket.close()
# tcp_server_socket.close()



# from socket import *
# tcp_server_socket=socket(AF_INET,SOCK_STREAM)
# addr=('',8080)
# tcp_server_socket.bind(addr)
# tcp_server_socket.listen(100)
# tcp_client_socket,tcp_client_ip=tcp_server_socket.accept()
# recv_from=tcp_client_socket.recv(1024)
# print(recv_from.decode('gbk'))
# print(tcp_client_ip)
# tcp_client_socket.close()
# tcp_server_socket.close()


# from socket import *
# tcp_socket=socket(AF_INET,SOCK_STREAM)
# addr=('192.168.1.6',8080)
# tcp_socket.connect(addr)
# tcp_socket.send('123'.encode('gbk'))
# rev=tcp_socket.recv(1024)
# print(rev.decode('gbk'))
# tcp_socket.close()


import urllib.request as a
response=a.urlopen('https://www.baidu.com')
headers=response.getheaders()
for x,y in headers:
    print(x,y)

html=response.read()
print(html)








