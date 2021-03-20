import socket
import mouse
import time
import threading


ip = "172.17.1.221"
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen()

client, address = server.accept()
print("Connection established at %s:%s" % (address[0], address[1]))

def broadcast(data):
    temp = str(data[0]) + "," + str(data[1])
    client.send(temp.encode())


def broadcastB(msg):
    time.sleep(0.5)
    client.send(msg.encode())

def mouseCapture():
    while True:
        time.sleep(0.05)
        a = mouse.get_position()
        broadcast(a)


threadA = threading.Thread(target=mouseCapture)
threadA.start()

while True:
    msg = input()
    if msg == "click":
        broadcastB(msg)
