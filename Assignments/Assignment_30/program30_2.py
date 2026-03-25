# //////////////////////////////////////////////////////////////////////////////////////
# //
# //  Function Name : CountWords
# //  Description   : It accepts a file name  from user and 
#                     returns the total number of words in the file
# //  Input         : String
# //  Ouput         : Integer
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 25/3/2026
# //
# //////////////////////////////////////////////////////////////////////////////////////

def CountWords(fName):
    fobj = open(fName,'r')
    iCnt = 0

    data = fobj.read()

    data = data.split()

    for word in data:
        iCnt+=1

    return iCnt
    

def main():
    fName = input("Enter name of File : ")

    iRet = CountWords(fName)

    print(f"Total number of words are : {iRet}")

if __name__ == "__main__":
    main()