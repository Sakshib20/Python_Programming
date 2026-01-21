# ///////////////////////////////////////////////////////////
# //
# //  Function Name : LMax
# //  Description   : It returns the maximum of two numbers
# //  Input         : Integer, Integer
# //  Ouput         : Integer
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 21/1/2026
# //
# ///////////////////////////////////////////////////////////

LMax = lambda No1,No2 : No1 if No1>No2 else No2

def main():
    Ret = LMax(13,9)
    print("Maximum is : ",Ret)

if __name__ == "__main__":
    main()

