import os
import sys
import schedule
import time

# //////////////////////////////////////////////////////////////////////////////////////
# //
# //  Function Name : DirScan
# //  Description   : It accepts a directory name and file extension from user and 
#                     displays all files with that extension
# //  Input         : String,String
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 03/04/2026
# //
# //////////////////////////////////////////////////////////////////////////////////////

def DirScan(dName,extName):
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
            for fName in FileName:
                if fName.endswith(extName):
                    fobj.write(fName)
                    fobj.write("\n")


def main():
    dName = sys.argv[1]
    extName = sys.argv[2]

    if(len(sys.argv) != 3):
        print("Please enter correct arguments")
        print("1 : Folder name")
        print("2 : Extension")
        return
    
    else:
        
        schedule.every(30).seconds.do(DirScan, sys.argv[1],sys.argv[2])

        while(True):
            schedule.run_pending()
            time.sleep(1)


if __name__ == "__main__":
    main()