# ///////////////////////////////////////////////////////////
# //
# //  Function Name : cpyContent
# //  Description   : Copies the content from one file to other
# //  Input         : String, String
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 13/3/2026
# //
# ///////////////////////////////////////////////////////////

import os

def cpyContent(f1,f2):
    try:
        fobj1 = open(f1,"r")

        Data = fobj1.read()
        
        fobj2 = open(f2,"w")
        fobj2.write(Data)
    
        print("------------ Data gets successfully written -----------") 

        fobj2.close()
        fobj1.close()

    except FileNotFoundError:
        print("File doesn't exists")

def main():
    file1 = input("Enter the name of Source File : ")
    file2 = input("Enter the name of destination file : ")

    cpyContent(file1,file2)

        
if __name__ == "__main__":
    main()