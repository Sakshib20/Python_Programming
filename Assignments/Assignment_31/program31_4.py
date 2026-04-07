import os
import sys
import schedule
import time
from pathlib import Path
import shutil

# ////////////////////////////////////////////////////////////////////////////////////////////////
# //
# //  Function Name : DirCpy
# //  Description   : It accepts two directory names and one file extension from user and 
# //                  copy all files with that extension from first directory to second directory 
# //  Input         : String, String
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 07/04/2026
# //
# ////////////////////////////////////////////////////////////////////////////////////////////////


def DirCpy(src,dest,ext):
    Ret = os.path.exists(src)

    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(src)

    if(Ret == False):
        print("Unable to scan as it's not a directory")
        return
    
    else:
        Ret = os.path.isdir(dest)

        if(Ret == False):
            os.mkdir(dest)

        for files in os.listdir(src):
            if(files.endswith(ext)):
                src_path = os.path.join(src,files)
                dest_path = os.path.join(dest,files)

                if os.path.isfile(src_path):
                    shutil.copy2(src_path,dest_path)
                


def main():
    Src_dName = sys.argv[1]
    Dest_dName = sys.argv[2]
    ext = sys.argv[3]

    if(len(sys.argv) != 4):
        print("Please enter correct arguments")
        print("1 : Directory Name")
        print("2 : Directory Name for Files to copy from 1st directory")
        print("3 : Extension name")
        return
    
    else:  
        schedule.every(10).seconds.do(DirCpy,sys.argv[1],sys.argv[2],sys.argv[3])

        while(True):
            schedule.run_pending()
            time.sleep(1)


if __name__ == "__main__":
    main()