# //////////////////////////////////////////////////////////////////////////////////////
# //
# //  Function Name : CountWords
# //  Description   : It accepts a file name  from user and 
#                     returns the number of line in the file
# //  Input         : String
# //  Ouput         : Integer
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 25/3/2026
# //
# //////////////////////////////////////////////////////////////////////////////////////

def CountLines(fName):
    fobj = open(fName,'r')
    iCnt = 0

    data = fobj.read()

    for word in data:
        if word == '\n':
            iCnt+=1

    return iCnt
    

def main():
    fName = input("Enter name of File : ")

    iRet = CountLines(fName)

    print(f"Total number of lines are : {iRet}")

if __name__ == "__main__":
    main()