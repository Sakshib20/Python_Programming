# ///////////////////////////////////////////////////////////
# //
# //  Function Name : openFile
# //  Description   : Displays the Content of file
# //  Input         : String
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 13/3/2026
# //
# ///////////////////////////////////////////////////////////

import os

def openFile(fname):
    try:
        fobj = open(fname,"r")

        Data = fobj.read()
        print("Data from file is : \n",Data)

        fobj.close()
    except FileNotFoundError:
        print("File doesn't exists")

def main():
    fName = input("Enter File Name : ")
   
    openFile(fName)
        
if __name__ == "__main__":
    main()