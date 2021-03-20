import socket
import mouse
import pyautogui

ip = "172.17.1.221"
port = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))


def receive():
    data = client.recv(1024)
    data = data.decode()
    if data == "click":
        pyautogui.click()
    else:
        a = data.split(',')
        mouse.move(a[0], a[1], absolute = True)


while True:
    receive()
