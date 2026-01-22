# ///////////////////////////////////////////////////////////
# //
# //  Function Name : ChkNum
# //  Description   : Checks if a number is positive, negative or zero
# //  Input         : Integer
# //  Ouput         : Void
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 22/1/2026
# //
# ///////////////////////////////////////////////////////////

def ChkNum(No):
    if No<0:
        print("Negative Number")
    elif No==0:
        print("Zero")
    else:
        print("Positive Number")

def main():
    Num = int(input("Enter Number :"))
    ChkNum(Num)

if __name__ == "__main__":
    main()

