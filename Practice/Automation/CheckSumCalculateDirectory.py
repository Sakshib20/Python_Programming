import hashlib
import os

def CalculateCheckSum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def DirectoryWatcher(DirectoryName = "Marvellous"):
    Ret = False

    Ret = os.path.exists(DirectoryName)

    if(Ret==False):
        print("There is no such directory")
        return
    else:
        Ret = os.path.isdir(DirectoryName)

        if(Ret==False):
            print("Its not a directory")
            return
    
    for FolderName, SubFolderName, Filename in os.walk(DirectoryName):
        for fName in Filename:
            fName = os.path.join(FolderName,fName)
            Checksum = CalculateCheckSum(fName)

            print(f"File name : {fName} CheckSum : {Checksum}")

def main():
    DirectoryWatcher()

if __name__=="__main__":
    main()