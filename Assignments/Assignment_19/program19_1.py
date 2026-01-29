# ///////////////////////////////////////////////////////////
# //
# //  Function Name : LSquare
# //  Description   : Returns power of 2
# //  Input         : Integer
# //  Ouput         : Integer
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 29/1/2026
# //
# ///////////////////////////////////////////////////////////


LSquare = lambda No : 2**No

def main():
    Value = int(input("Enter the number : "))
    Ret = LSquare(Value)
    print(Ret)

if __name__ == "__main__":
    main()

