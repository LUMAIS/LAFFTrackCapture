import os.path
from helperFunctions.connect import connection

def createFile(path,fileName, format):
    name = path+connection+fileName+'.'+format
    file_exists = os.path.exists(name)
    n=0
    while file_exists:
        name = path+connection+fileName+'_'+str(n)+'.'+format
        file_exists = os.path.exists(name)
        n=n+1

    return name