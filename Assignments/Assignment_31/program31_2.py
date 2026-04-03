import os
import sys
import schedule
import time
from pathlib import Path

# ////////////////////////////////////////////////////////////////////////////////////////////////
# //
# //  Function Name : DirRename
# //  Description   : It accepts a directory name and two file extensions from user and 
#                     rename all files with first file extension with second file extension
# //  Input         : String
# //  Ouput         : Integer
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 03/04/2026
# //
# ////////////////////////////////////////////////////////////////////////////////////////////////


def DirRename(dName,src,dest):
    Ret = os.path.exists(dName)

    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(dName)

    if(Ret == False):
        print("Unable to scan as it's not a directory")
        return
    
    else:

        for FolderName, SubFolder, FileName in os.walk(dName):
            for fName in FileName:
                if fName.endswith(src):
                    fPath = Path(FolderName)/fName
                    fPath.rename(fPath.with_suffix(dest))


def main():
    dName = sys.argv[1]
    ext1 = sys.argv[2]
    ext2 = sys.argv[3]

    if(len(sys.argv) != 4):
        print("Please enter correct arguments")
        print("1 : Folder name")
        print("2 : Original Extension")
        print("3 : Replacement Extension : ")
        return
    
    
    else:
        
        schedule.every(30).seconds.do(DirRename,sys.argv[1],sys.argv[2],sys.argv[3])

        while(True):
            schedule.run_pending()
            time.sleep(1)
        

if __name__ == "__main__":
    main()