# ///////////////////////////////////////////////////////////
# //
# //  Function Name : CountDigits 
# //  Description : It prints counts of digits in a number
# //  Input :   Integer
# //  Ouput :   void
# //  Author : Sakshi Pradeep Bhapkar
# //  Date : 19/1/2026
# //
# ///////////////////////////////////////////////////////////

def CountDigits(No):
    iCnt = 0
    while(No!=0):
        iCnt = iCnt+1
        No = No//10

    print(iCnt)

def main():
    CountDigits(721)

if __name__ == "__main__":
    main()