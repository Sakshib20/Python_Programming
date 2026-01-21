# ///////////////////////////////////////////////////////////
# //
# //  Function Name : LCheckEven
# //  Description   : It checks whether a number is even
# //  Input         : Integer
# //  Ouput         : Integer
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 21/1/2026
# //
# ///////////////////////////////////////////////////////////

LCheckEven = lambda No : True if No%2==0 else False

def main():
    Ret = LCheckEven(998)
    print(Ret)

if __name__ == "__main__":
    main()

