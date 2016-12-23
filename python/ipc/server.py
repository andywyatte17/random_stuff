# Echo server program
from __future__ import print_function
import socket
import turtle

def flush_one(data):
    x = data.find('\n')
    if x>=0:
        cmd = data[:x+1]
        print(cmd, end='')
        if cmd.startswith('turtle.'):
            exec(cmd)
        return data[x+1:]
    return data

HOST = '127.0.0.1'        # Symbolic name meaning all available interfaces
PORT = 50008              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
last = ""
while 1:
    data = conn.recv(8)
    if not data:
        last = flush_one(last+data)
        continue
    conn.sendall(data)
    last = flush_one(last+data)
conn.close()
