import os


def shellbomb():
    f = open("shellbomb.bat", "w")
    f.write("start")
    f.close()
    os.system("shellbomb.bat")
