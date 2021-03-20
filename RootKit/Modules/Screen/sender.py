from vidstream import ScreenShareClient


sender = ScreenShareClient("192.168.1.79", 55555)
sender.start_stream()
