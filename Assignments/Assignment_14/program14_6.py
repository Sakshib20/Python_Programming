# ///////////////////////////////////////////////////////////
# //
# //  Function Name : LCheckOdd
# //  Description   : It checks whether a number is odd
# //  Input         : Integer
# //  Ouput         : Integer
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 21/1/2026
# //
# ///////////////////////////////////////////////////////////

LCheckOdd = lambda No : True if No%2!=0 else False

def main():
    Ret = LCheckOdd(995)
    print(Ret)

if __name__ == "__main__":
    main()

