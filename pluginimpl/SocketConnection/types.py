class types:
    addr="172.31.1.88"
    inb=b''
    outb=b''
    def __init__(self):
        addr="172.31.1.88"
        inb=b''
        outb=str.encode("test")
    def SimpleNamespace(address, inb, outb):
        addr=address
        inb=inb
        outb=outb
        return types
