# ///////////////////////////////////////////////////////////
# //
# //  Function Name : DisplayRev
# //  Description : It prints number in reverse
# //  Input :   Integer
# //  Ouput :   void
# //  Author : Sakshi Pradeep Bhapkar
# //  Date : 19/1/2026
# //
# ///////////////////////////////////////////////////////////

def DisplayRev(No):
    while(No!=0):
        digit = No%10
        print(digit,end="")
        No = No//10

def main():
    DisplayRev(123)

if __name__ == "__main__":
    main()