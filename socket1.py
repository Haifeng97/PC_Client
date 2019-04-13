import socket

client = socket.socket()
#port = input()
client.connect(('192.168.1.147', 1586))
i = 1
while 1:
    print('seq:', i)
    i += 1
    ret = str(client.recv(1024), encoding='utf-8')
    print(ret)