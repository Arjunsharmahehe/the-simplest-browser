from socket import *

mysocket = socket(AF_INET, SOCK_STREAM)
mysocket.connect(('data.pr4e.org', 80))
command = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
mysocket.send(command)

while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    else:
        print(data.decode(), end='')

mysocket.close()