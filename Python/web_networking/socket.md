## Sockets
Python has built-in support for TCP sockets
HTTP - The HyperText Transfer Protocol is the set of rules to allow browsers to retrieve web documents  
from servers over the Internet

````
http://  www.cookieMonster.com   /page1.htm
protocol      host                 document
````

````python
import socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating socket AF_INET = IPv4 SOCK_STREAM = TCP socket 
my_socket.connect(('data.pr4e.org', 80)) # host is like a phone number, port is like a phone extension
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
my_socket.send(cmd)

while True:
    data = my_socket.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
my_socket.close()
````





