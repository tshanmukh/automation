import socket
import selectors

sel = selectors.DefaultSelector()

HOST = "172.31.1.88"
PORT = 1111

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.setblocking(False)
lsock.connect((HOST,PORT))
events = selectors.EVENT_READ | selectors.EVENT_WRITE

sel.register(lsock, selectors.EVENT_READ, data=None)

while True:
    events = sel.select(timeout=None)
    for key, mask in events:
        if key.data is None:
            # accept_wrapper(key.fileobj)
            print("Code is here")
        else:
            sock = key.fileobj
            data = key.data
            if mask & selectors.EVENT_READ:
                recv_data = sock.recv(1024)  # Should be ready to read
                if recv_data:
                    print('received', repr(recv_data), 'from connection', data.connid)
                    data.recv_total += len(recv_data)
                if not recv_data or data.recv_total == data.msg_total:
                    print('closing connection', data.connid)
                    sel.unregister(sock)
                    sock.close()
            if mask & selectors.EVENT_WRITE:
                if not data.outb and data.messages:
                    data.outb = data.messages.pop(0)
                if data.outb:
                    print('sending', repr(data.outb), 'to connection', data.connid)
                    sent = sock.send(data.outb)  # Should be ready to write
                    data.outb = data.outb[sent:]