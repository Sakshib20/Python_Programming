# ///////////////////////////////////////////////////////////
# //
# //  Function Name : DisplayLen
# //  Description   : Displays length of a string
# //  Input         : String
# //  Ouput         : Integer
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 22/1/2026
# //
# ///////////////////////////////////////////////////////////

def DisplayLen(Name):
    return len(Name)

def main():
    sValue=input("Enter the name :")
    DisplayLen(sValue)

    Ret = DisplayLen(sValue)
    print(Ret)

if __name__ == "__main__":
    main()

