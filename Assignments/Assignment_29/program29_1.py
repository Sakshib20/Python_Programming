# ///////////////////////////////////////////////////////////
# //
# //  Function Name : ChkIsExists
# //  Description   : Checks if the file exists in current directory or not 
# //  Input         : String
# //  Ouput         : Boolean
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 13/3/2026
# //
# ///////////////////////////////////////////////////////////

import os

def ChkIsExists(fName):
    Ret = os.path.exists(fName)

    return Ret

def main():
    fName = input("Enter File Name : ")
    bRet = False

    bRet = ChkIsExists(fName)
    
    if(bRet == True):
        print("File Exists")
    else:
        print("File does not exits")

if __name__ == "__main__":
    main()