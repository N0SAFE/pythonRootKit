from vidstream import StreamingServer
import threading

receiver = StreamingServer("192.168.1.79", 55556)
t = threading.Thread(target=receiver.start_server)
t.start()

while input() != "stop":
    continue

receiver.stop_server()