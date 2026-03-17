import sys
import os

def DirectoryScanner(DirName = "Marvellous"):
    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such Directory")
        return

    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    for FolderName , SubFolder , FileName in os.walk(DirName):
        for fname in FileName:
            print("FileName : ",fname)
            print("File size : " ,os.path.getsize(fname))           # Path issue
            
def main():
    Boarder = "-"*50
    print(Boarder)
    print("-----------Marvellous Directory Automation-----------")
    print(Boarder)

    if(len(sys.argv) != 2):
        print("Invalid number of argument")
        print("Please specify the name og directory")
        return
    
    DirectoryScanner(sys.argv[1])

if __name__ == "__main__": 
    main()
    