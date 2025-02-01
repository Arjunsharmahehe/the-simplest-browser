from socket import *

# inits a socket
mysocket = socket(AF_INET, SOCK_STREAM)

# forms the connection with the server (domain name, port )
mysocket.connect(('data.pr4e.org', 80))

# the telnet command that we send
# .encode() encodes the UNICODE string to UTF-8 
command = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()

# sending that command to the server
mysocket.send(command)

while True:
    # reading the data in small packages (the server might be slow)
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    else:
        print(data.decode(), end='')

# closing the socket from our side
mysocket.close()