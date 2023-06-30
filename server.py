#!/user/bin/env python
#_*_ codign: utf8 _*_

import socket

def upserver():
    global server
    global ip
    global target

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('192.168.20.109',7777))
    server.listen(1)

    print("Corriendo el servidor")

    target, ip = server.accept()
    print("Conexion recibida de: " + str(ip[0]))

upserver()
server.close()