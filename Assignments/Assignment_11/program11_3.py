# ///////////////////////////////////////////////////////////
# //
# //  Function Name : SumDigits 
# //  Description : It prints sum of digits in a number
# //  Input :   Integer
# //  Ouput :   void
# //  Author : Sakshi Pradeep Bhapkar
# //  Date : 19/1/2026
# //
# ///////////////////////////////////////////////////////////

def SumDigits(No):
    Sum = 0
    while(No!=0):
        digit = No%10
        Sum = Sum+digit
        No = No//10

    print(Sum)

def main():
    SumDigits(123)

if __name__ == "__main__":
    main()