#发送数据

# from socket import *
# udp_socket=socket(AF_INET,SOCK_DGRAM)
# socket_data=input('请输入你要发送的数据：')
# s=('192.168.1.3',8080)
# udp_socket.sendto(socket_data.encode('gb2312'),s)
# udp_socket.close()

#发送接收数据
# from socket import *
#
# # 1. 创建udp套接字
# udp_socket = socket(AF_INET, SOCK_DGRAM)
# # 2. 准备接收方的地址
# dest_addr = ('192.168.1.3', 8080)
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


from socket import *

# 创建socket
tcp_client_socket = socket(AF_INET, SOCK_STREAM)

# 目的信息
server_addr = ('192.168.1.254', 8080)
# 链接服务器
tcp_client_socket.connect(server_addr)

# 提示用户输入数据
send_data = input("请输入要发送的数据：")

tcp_client_socket.send(send_data.encode("gbk"))

# 接收对方发送过来的数据，最大接收1024个字节
recvData = tcp_client_socket.recv(1024)
print('接收到的数据为:', recvData.decode('gbk'))

# 关闭套接字
tcp_client_socket.close()


# from socket import *
#
# # 1. 创建套接字
# udp_socket = socket(AF_INET, SOCK_DGRAM)
#
# # 2. 绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
# local_addr = ('', 7788)  # ip地址和端口号，ip一般不用写，表示本机的任何一个ip
# udp_socket.bind(local_addr)
#
# # 3. 等待接收对方发送的数据
# recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
#
# # 4. 显示接收到的数据
# print(recv_data[0].decode('gb2312'))
#
# # 5. 关闭套接字
# udp_socket.close()














