import os
import sys
import hashlib
import schedule
import time

# ////////////////////////////////////////////////////////////////////////////////////////////////
# //
# //  Function Name : DirectoryDuplicateRemoval
# //  Description   : It accepts a directory name from user and delete all duplicate files from
# //                  that directory. Writes names of duplicate files from directory into 
# //                  log file named as Log.txt
# //  Input         : String
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 07/04/2026
# //
# ////////////////////////////////////////////////////////////////////////////////////////////////


def DirectoryDuplicateRemoval(dName):
    myDict = DirectoryDuplicate(dName)

    fobj = open("Log.txt","w")

    Result = list(filter(lambda X : (len(X)>1),myDict.values()))

    Count = 0
    Cnt = 0

    for value in Result:
        for subvalue in value:
            Count = Count+1
            
            if(Count>1):
                fobj.write(f"{subvalue}\n")
                os.remove(subvalue)

                Cnt = Cnt+1
        Count = 0

    fobj.write(f"Total deleted files : {Cnt}") 


def CalculateCheckSum(filename):
    fobj = open(filename,'rb')

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def DirectoryDuplicate(dName):
    Ret = os.path.exists(dName)

    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(dName)

    if(Ret == False):
        print("Unable to scan as it's not a directory")
        return
    
    else:
        Duplicate = {}

        fobj = open("Log.txt",'w')
        for FolderName, SubFolder, FileName in os.walk(dName):
            for file in FileName:
                file = os.path.join(FolderName,file)
                Checksum = CalculateCheckSum(file)

                if Checksum in Duplicate:
                    Duplicate[Checksum].append(file)
                else:
                    Duplicate[Checksum] = [file]
    
        return Duplicate
            

def main():
    dName = sys.argv[1]

    if(len(sys.argv) != 2):
        print("Please enter correct arguments")
        print("1 : Directory Name")
        return
    
    else:
        
        schedule.every(10).seconds.do(DirectoryDuplicateRemoval,sys.argv[1])

        while(True):
            schedule.run_pending()
            time.sleep(1)

        

if __name__ == "__main__":
    main()