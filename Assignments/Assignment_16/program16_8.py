# ///////////////////////////////////////////////////////////
# //
# //  Function Name : Display
# //  Description   : Displays userdefined number of "*" on screen
# //  Input         : Integer
# //  Ouput         : Void
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 22/1/2026
# //
# ///////////////////////////////////////////////////////////

def Display(No):
    for i in range(No):
        print("*\t",end="")
       

def main():
    Num = int(input("Enter Number :"))
    Display(Num)

if __name__ == "__main__":
    main()

