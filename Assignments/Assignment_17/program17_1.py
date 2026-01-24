# ///////////////////////////////////////////////////////////
# //
# //  Function Name : Fun
# //  Description   : Displays a hello message 
# //  Input         : Void
# //  Ouput         : Void
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 24/1/2026
# //
# ///////////////////////////////////////////////////////////

import MyModule

def main():

    Value1 = int(input("Enter 1st number :"))
    Value2 = int(input("Enter 2nd number :"))

    Ret = MyModule.Add(Value1,Value2)
    print("Addition is :",Ret)

    Ret = MyModule.Sub(Value1,Value2)
    print("Substraction is :",Ret)

    Ret = MyModule.Mult(Value1,Value2)
    print("Multiplication is :",Ret)

    Ret = MyModule.Div(Value1,Value2)
    print("Division is :",Ret)


if __name__ == "__main__":
    main()

