from fileinput import filename
import requests
import zipfile
import os
import shutil
import time

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
def supFile(data):
    if type(data) == list:
        for i in range(len(data)):
            if data[i-1] != getFileName():
                try:
                    os.remove(data[i-1])
                except:
                    None
    if type(data) == str:
        if data != getFileName():
            try:
                os.remove(data)
            except:
                None

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
    fichiers = sortNameFile(data)
    for f in range(len(fichiers)):
        if fichiers[f] != getFileName():
            path = getpath(True)
            path = path+"/"+data+"/"+fichiers[f]
            shutil.copy(path, getpath(True))

def executeFile(data):
    os.system(data)

def update(data, delete=False):
    '''
    this methode can only be used for download file from github.com
    
    data = link of the web depository
    
    you can also use the delete args
    
    if delete = True all the files in the folder will be deleted then replaced by what has been downloaded
    '''
    dir = getNameDir(data)
    if delete in (True, "true", "vrai"):
        supFile(sortNameFile(getpath(True)))
    downloadFileGithub(data)
    moveFileFromDir(dir)
    supDir(dir)
