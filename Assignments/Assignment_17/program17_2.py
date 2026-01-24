# ///////////////////////////////////////////////////////////
# //
# //  Function Name : Display
# //  Description   : Displays user defined number os "*" on the screen
# //  Input         : Integer
# //  Ouput         : Void
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 24/1/2026
# //
# ///////////////////////////////////////////////////////////

def Display(No):
    iCnt = 0

    while(iCnt!=No):
        for i in range(No):
            print("*\t",end="")
        print()
        iCnt+=1

def main():
    Value = int(input("Enter number :"))

    Display(Value)
    

if __name__ == "__main__":
    main()

