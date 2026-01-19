# ///////////////////////////////////////////////////////////
# //
# //  Function Name : DivByThreeandFive 
# //  Description : It is used to check whether a number is divisible by 3 and 5
# //  Input :   Integer
# //  Ouput :   Void
# //  Author : Sakshi Pradeep Bhapkar
# //  Date : 19/1/2026
# //
# ///////////////////////////////////////////////////////////

def DivByThreeandFive(No):
    if (No%3 == 0 and No%5==0):
        print("Divisible by 3 and 5")
    
    else:
        print("Not divisible by 3 and 5")


def main():
    DivByThreeandFive(25)

if __name__ == "__main__":
    main()