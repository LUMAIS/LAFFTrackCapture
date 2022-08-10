import os.path
from helperFunctions.connect import connection

# Takes: str path 
def createFile(path,fileName, format):
    """Path(str): direction to path to save file
    fileName (str): name of the file
    format(str): to be appended. No need of '.'
    """
    name = path+connection+fileName+'.'+format
    file_exists = os.path.exists(name)
    n=0
    while file_exists:
        name = path+connection+fileName+'_'+str(n)+'.'+format
        file_exists = os.path.exists(name)
        n=n+1

    return name