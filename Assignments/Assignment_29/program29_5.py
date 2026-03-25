# ///////////////////////////////////////////////////////////
# //
# //  Function Name : Freq
# //  Description   : It accepts a file name and string from
#                     user and returns the frequency of that string in the file
# //  Input         : String, String
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 13/3/2026
# //
# ///////////////////////////////////////////////////////////

def Freq(fName, word):
    iCnt = 0
    try:
        fobj = open(fName,"r")

        Data = fobj.read()

        wList = Data.split()
        
        for i in wList:
            if i == word:
                iCnt = iCnt+1

    except FileNotFoundError:
        print("File doesn't exists")

    return iCnt
    

def main():
    fName = input("Enter name of File : ")
    word = input("Enter the String : ")

    iRet = Freq(fName,word)

    print(f"{word} count is : {iRet}")

if __name__ == "__main__":
    main()