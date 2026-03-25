# //////////////////////////////////////////////////////////////////////////////////////
# //
# //  Function Name : ChkWord
# //  Description   : It accepts a file name and word  from user and 
#                     checks if that word is present in the file or not
# //  Input         : String
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 25/3/2026
# //
# //////////////////////////////////////////////////////////////////////////////////////

def ChkWord(fName,search):

    bFlag = False
    fobj = open(fName,"r")
    data = fobj.read()
    data = data.split()

    for word in data:
        if (word.casefold() == search.casefold()):
            bFlag = True

    return bFlag
            
    
def main():
    fName = input("Enter the name of File : ")
    word = input("Enter the word to search : ")

    bRet = ChkWord(fName,word)

    if(bRet == True):
        print("Word is present")

    else:
        print("Word is not present")

if __name__ == "__main__":
    main()