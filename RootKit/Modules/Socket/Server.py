import socket

ip = "127.0.0.1"
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen()


client, address = server.accept()
print("Connection established at %s:%s" % (address[0], address[1]))

def broadcast(data):
    client.send(data.encode("ascii"))


while True:
    broadcast(input(">"))
