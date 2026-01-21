# ///////////////////////////////////////////////////////////
# //
# //  Function Name : LMax
# //  Description   : It returns the maximum of three numbers
# //  Input         : Integer, Integer
# //  Ouput         : Integer
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 21/1/2026
# //
# ///////////////////////////////////////////////////////////

LMax = lambda No1,No2,No3 : No1 if No1>No2 and No1>No3 else No2 if No2>No1 and No2>No3 else No3

def main():
    Ret = LMax(13,121,11)
    print("Maximum is : ",Ret)

if __name__ == "__main__":
    main()

