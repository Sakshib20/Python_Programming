# ///////////////////////////////////////////////////////////
# //
# //  Function Name : Factorial
# //  Description   : Returns Factorial of a number
# //  Input         : Integer
# //  Ouput         : Integer
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 24/1/2026
# //
# ///////////////////////////////////////////////////////////

def Factorial(No):
    Fact = 1
    for i in range(1,No+1):
        Fact = Fact*i

    return Fact

def main():
    Value = int(input("Enter number :"))

    Ret = Factorial(Value)
    print("Factorial is :",Ret)
    

if __name__ == "__main__":
    main()

