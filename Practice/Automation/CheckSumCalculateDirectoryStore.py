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

def FindDuplicate(DirectoryName = "Marvellous"):
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
        
    Duplicate = {}
    
    for FolderName, SubFolderName, Filename in os.walk(DirectoryName):
        for fName in Filename:
            fName = os.path.join(FolderName,fName)
            Checksum = CalculateCheckSum(fName)

            if Checksum in Duplicate:
                Duplicate[Checksum].append(fName)
            else:
                Duplicate[Checksum] = [fName]
    return Duplicate

def DisplayResult(myDict):
    Result = list(filter(lambda X : (len(X)>1),myDict.values()))

    Count = 0

    for value in Result:
        for subvalue in value:
            Count = Count+1
            print(subvalue)
        print("Value of count : ",Count)
        Count = 0

def DeleteDuplicate(path = "Marvellous"):
    myDict = FindDuplicate(path)

    Result = list(filter(lambda X : (len(X)>1),myDict.values()))

    Count = 0
    Cnt = 0

    for value in Result:
        for subvalue in value:
            Count = Count+1
            
            if(Count>1):
                print("Deleted file : ",subvalue)
                os.remove(subvalue)

                Cnt = Cnt+1
        Count = 0

    print("Total deleted files : ",Cnt)    
        


def main():
    DeleteDuplicate()

if __name__=="__main__":
    main()