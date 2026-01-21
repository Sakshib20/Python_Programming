# ///////////////////////////////////////////////////////////
# //
# //  Function Name : LCheckDivByFive
# //  Description   : It checks whether a number is divisible by 5
# //  Input         : Integer
# //  Ouput         : Integer
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 21/1/2026
# //
# ///////////////////////////////////////////////////////////

LCheckDivByFive = lambda No : True if No%5==0 else False

def main():
    Ret = LCheckDivByFive(995)
    print(Ret)

if __name__ == "__main__":
    main()

