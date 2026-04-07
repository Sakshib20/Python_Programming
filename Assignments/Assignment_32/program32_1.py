import os
import sys
import hashlib
import schedule
import time


def CalculateCheckSum(filename):
    fobj = open(filename,'rb')

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

# ////////////////////////////////////////////////////////////////////////////////////////////////
# //
# //  Function Name : DirectoryCheckSum
# //  Description   : It accepts a directory name from user and display checksum of all files
# //  Input         : String
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 03/04/2026
# //
# ////////////////////////////////////////////////////////////////////////////////////////////////

def DirectoryCheckSum(dName):
    Ret = os.path.exists(dName)

    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(dName)

    if(Ret == False):
        print("Unable to scan as it's not a directory")
        return
    
    else:

        fobj = open("Marvellous.log",'w')
        for FolderName, SubFolder, FileName in os.walk(dName):
            for file in FileName:
                file = os.path.join(FolderName,file)
                Checksum = CalculateCheckSum(file)

                fobj.write(f"File name : {file}  Checksum : {Checksum}\n")


def main():
    dName = sys.argv[1]

    if(len(sys.argv) != 2):
        print("Please enter correct arguments")
        print("1 : Directory Name")
        return
    
    else:
        
        schedule.every(10).seconds.do(DirectoryCheckSum,sys.argv[1])

        while(True):
            schedule.run_pending()
            time.sleep(1)

        

if __name__ == "__main__":
    main()