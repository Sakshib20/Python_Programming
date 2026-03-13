# ///////////////////////////////////////////////////////////
# //
# //  Function Name : Cmpr
# //  Description   : Compares the content of file, if contents are same it displays Success, else it displays Failure
# //  Input         : String, String
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 13/3/2026
# //
# ///////////////////////////////////////////////////////////

import hashlib
import sys

def Cmpr(f1,f2):
    fobj1 = open(f1,"rb")

    hobj1 = hashlib.md5()

    Buffer1 = fobj1.read(1000)

    while( len(Buffer1)>0):
        hobj1.update(Buffer1)
        Buffer1 = fobj1.read(1000)

    C1 = hobj1.hexdigest()

    fobj2 = open(f2,"rb")

    hobj2 = hashlib.md5()

    Buffer2 = fobj2.read(1000)

    while( len(Buffer2)>0):
        hobj2.update(Buffer2)
        Buffer2 = fobj2.read(1000)

    C2 = hobj2.hexdigest()

    if(C1==C2):
        print("Success")
    else:
        print("Failure")
    

def main():
    
    for i in range(len(sys.argv)):
        file1 = sys.argv[1]
        file2 = sys.argv[2]

    Cmpr(file1,file2)

if __name__ == "__main__":
    main()