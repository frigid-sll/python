# from socket import *
# udp_socket=socket(AF_INET,SOCK_DGRAM)
# print(1)
# udp_socket.close()

# from socket import *
# udp_socket=socket(AF_INET,SOCK_DGRAM)
# udp_addr=('192.168.1.6',8080)
# content=input('请输入你要发送的内容：')
# udp_socket.sendto(content.encode('gb2312'),udp_addr)
# udp_socket.close()

# from socket import *
# udp_socket=socket(AF_INET,SOCK_DGRAM)
# addr=('192.168.1.228',8080)
# content=input("请输入你要发送的内容：")
# udp_socket.sendto(content.encode('gb2312'),addr)
# recv_data=udp_socket.recvfrom(1024)
# print(recv_data[0].decode('gb2312'))
# print(recv_data[1])
# udp_socket.close()

# from socket import *
# udp_socket=socket(AF_INET,SOCK_DGRAM)
# addr=('',7788)
# udp_socket.bind(addr)
# content=input("请输入你要发送的内容：")
# udp_socket.sendto(content.encode('gb2312'),('192.168.1.228',8080))
# revc_data=udp_socket.recvfrom(1024)
# print(revc_data[0].decode('gb2312'))
# udp_socket.close()


# alist=[1,2,3,4,5]
# def cha(n,item):
#     if len(n)==0:
#         return False
#     else:
#         x=len(n)//2
#         if n[x]==item:
#             return True
#         elif item>n[x]:
#             return cha(n[x+1:],item)
#         else:
#             return cha(n[:x],item)
# print(cha(alist,8))

# from socket import *
# udp_socket=socket(AF_INET,SOCK_DGRAM)
# content=input('请输入你要穿的内容：')
# udp_socket.sendto(content.encode('gbk'),('192.168.1.1',8080))
# recv_from,s=udp_socket.recvfrom(1024)
# print(recv_from.decode('gbk'))
# print(s)
# udp_socket.close()


# from socket import *
# tcp_1=socket(AF_INET,SOCK_STREAM)
# addr=('192.168.1.6',8080)
# tcp_1.bind(addr)
# tcp_1.listen(100)
# q,w=tcp_1.accept()
# recv_from=q.recv(1024)
# print(recv_from.decode('gbk'))
# q.send('正在处理中...'.encode('gbk'))
# q.close()
# tcp_1.close()




# from socket import *
# udp=socket(AF_INET,SOCK_DGRAM)
# addr=('',7788)
# udp.bind(addr)
# data=input("请输入你要发送的内容：")
# udp.sendto(data.encode('gbk'),('192.168.1.6',8080))
# recv,ip=udp.recvfrom(1024)
# print('收到的信息为：%s'%recv.decode('gbk'))
# print(ip)
# udp.close()


#
# from socket import *
# udp_socket=socket(AF_INET,SOCK_DGRAM)
# addr=('',8080)
# udp_socket.bind(addr)
# data=input('请输入你要发送的内容：')
# udp_socket.sendto(data.encode('gbk'),('192.168.1.6',7788))
# recv_from,ip=udp_socket.recvfrom(1024)
# print('收到的消息为：%s'%recv_from.decode('gbk'))
# udp_socket.close()





# import urllib.request as a
# response=a.urlopen('https://www.baidu.com')
# header=response.getheaders()
# for x,y in header:
#     print(x,y)
# html=response.read()
# print(html)





