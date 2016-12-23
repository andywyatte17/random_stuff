# Echo client program
import socket

HOST = '127.0.0.1'        # The remote host
PORT = 50008              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    x = raw_input()
    if x=='':
       break
    s.sendall(x + '\n')
s.close()
print 'Received', repr(data)
