# ///////////////////////////////////////////////////////////
# //
# //  Function Name : LMin
# //  Description   : It returns minimum of two numbers
# //  Input         : Integer, Integer
# //  Ouput         : Integer
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 21/1/2026
# //
# ///////////////////////////////////////////////////////////

LMin = lambda No1,No2 : No1 if No1<No2 else No2

def main():
    Ret = LMin(13,9)
    print("Minimum is : ",Ret)

if __name__ == "__main__":
    main()

