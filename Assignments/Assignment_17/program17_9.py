# ///////////////////////////////////////////////////////////
# //
# //  Function Name : CountDigits
# //  Description   : Returns number of digits in a number
# //  Input         : Integer
# //  Ouput         : Integer
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 24/1/2026
# //
# ///////////////////////////////////////////////////////////

def CountDigits(No):
    Cnt = 0

    while(No != 0):
        Cnt+=1
        No=No//10

    return Cnt

def main():
    Value = int(input("Enter number :"))

    Ret = CountDigits(Value)
    print(Ret)
   
if __name__ == "__main__":
    main()

