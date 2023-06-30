#!/user/bin/env python
#_*_ codign: utf8 _*_

import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("192.168.20.109",7777))
cliente.close()