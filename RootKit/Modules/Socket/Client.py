import socket

ip = "127.0.0.1"
port = 55555
run = True

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))


def receive():
    data = client.recv(1024)
    print(data.decode("ascii"))
    return data.decode("ascii")


def execute(data):
    global run
    if data == "die":
        run = False

while run == True:
    execute(receive())
