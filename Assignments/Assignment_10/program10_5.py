# ///////////////////////////////////////////////////////////
# //
# //  Function Name : DisplayOdd
# //  Description : It is used to print all odd numbers till a given number
# //  Input :   Integer
# //  Ouput :   Void
# //  Author : Sakshi Pradeep Bhapkar
# //  Date : 19/1/2026
# //
# ///////////////////////////////////////////////////////////

def DisplayOdd(No):
    for i in range(1,No+1):
        if (i%2 != 0):
            print(i,"\t",end="")


def main():
    DisplayOdd(11)

if __name__ == "__main__":
    main()