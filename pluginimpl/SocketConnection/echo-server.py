import socket

HOST = '172.31.1.88'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data)
            if data.startswith(str.encode("ACT-USER")):
                conn.sendall(str.encode(''))
                # conn.close()

            conn.sendall(data)