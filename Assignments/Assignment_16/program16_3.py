# ///////////////////////////////////////////////////////////
# //
# //  Function Name : Add
# //  Description   : Returns Addition of two numbers
# //  Input         : Integer, Integer
# //  Ouput         : Integer
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 22/1/2026
# //
# ///////////////////////////////////////////////////////////

def Add(No1,No2):
    return No1+No2

def main():
    Num1 = int(input("Enter 1st Number :"))
    Num2 = int(input("Enter 2nd Number :"))

    Ret = Add(Num1,Num2)

    print("Addition is :",Ret)

if __name__ == "__main__":
    main()

