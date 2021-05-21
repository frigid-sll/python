# from socket import *
# udp_socket=socket(AF_INET,SOCK_DGRAM)
# addr=('192.168.1.6',8080)
# udp_socket.sendto('你就是个垃圾'.encode('gbk'),addr)
# ret=udp_socket.recvfrom(1000)
# print(ret[0].decode('gbk'),ret[1])
# udp_socket.close()

# from socket import *
# tcp_server_socket=socket(AF_INET,SOCK_STREAM)
# addr=('192.168.1.6',8080)
# tcp_server_socket.connect(addr)
# tcp_server_socket.send('你好纯哦'.encode('gbk'))
# ret=tcp_server_socket.recv(1000)
# print(ret.decode('gbk'))
# tcp_server_socket.close()

# from socket import *
# tcp_server_socket=socket(AF_INET,SOCK_STREAM)
# addr=('192.168.32.1',8080)
# tcp_server_socket.bind(addr)
# tcp_server_socket.listen(100)
# tcp_client_socket,tcp_client_ip=tcp_server_socket.accept()
# tcp_client_socket.send('你好傻哦'.encode('gbk'))
# ret=tcp_client_socket.recv(1000)
# print(ret.decode('gbk'))
# tcp_client_socket.close()
# tcp_server_socket.close()









