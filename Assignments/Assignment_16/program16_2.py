# ///////////////////////////////////////////////////////////
# //
# //  Function Name : ChkNum
# //  Description   : If number is even it display "Even Number" otherwise it displays "Odd Number" 
# //  Input         : Integer
# //  Ouput         : Void
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 22/1/2026
# //
# ///////////////////////////////////////////////////////////

def ChkNum(No):
    if No%2==0:
        print("Even Number")
    else:
        print("Odd Number")

def main():
    Num = int(input("Enter Number :"))
    ChkNum(Num)

if __name__ == "__main__":
    main()

