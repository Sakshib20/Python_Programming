# ///////////////////////////////////////////////////////////
# //
# //  Function Name : FactAdd
# //  Description   : Returns Factorial of a number
# //  Input         : Integer
# //  Ouput         : Integer
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 24/1/2026
# //
# ///////////////////////////////////////////////////////////

def FactAdd(No):
    Sum = 0

    for i in range(1,(No//2)+1):
        if(No%i==0):
            Sum = Sum+i
    return Sum    

def main():
    Value = int(input("Enter number :"))

    Ret = FactAdd(Value)
    print("Addition of Factors is :",Ret)
    

if __name__ == "__main__":
    main()

