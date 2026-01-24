# ///////////////////////////////////////////////////////////
# //
# //  Function Name : SumDigits
# //  Description   : Returns the sum of digits in a number
# //  Input         : Integer
# //  Ouput         : Integer
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 24/1/2026
# //
# ///////////////////////////////////////////////////////////

def SumDigits(No):
    Sum = 0

    while(No != 0):
        Digit = No%10
        Sum = Sum+ Digit
        No=No//10

    return Sum

def main():
    Value = int(input("Enter number :"))

    Ret = SumDigits(Value)
    print(Ret)
   
if __name__ == "__main__":
    main()

