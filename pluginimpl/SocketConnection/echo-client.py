import socket

HOST = '172.31.1.88'
PORT = 1111

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.setblocking(False)
    for i in range(1000):
        s.sendall(b'act-user:::1;')
        data=s.recv(1024)
        print("Received the following data", repr(data),"\n")
        s.sendall(b';import::tx-coe:1;')
        data = s.recv(1024)
        print("Received the following data", repr(data))
