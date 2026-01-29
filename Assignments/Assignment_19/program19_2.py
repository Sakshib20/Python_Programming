# ///////////////////////////////////////////////////////////
# //
# //  Function Name : LMult
# //  Description   : Returns multiplication of two numbers
# //  Input         : Integer, Integer
# //  Ouput         : Integer
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 29/1/2026
# //
# ///////////////////////////////////////////////////////////


LMult = lambda No1, No2 : No1*No2

def main():
    Value1 = int(input("Enter the  number : "))
    Value2 = int(input("Enter the  number : "))

    Ret = LMult(Value1,Value2)
    print(Ret)

if __name__ == "__main__":
    main()

