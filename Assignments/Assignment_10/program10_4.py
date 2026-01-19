# ///////////////////////////////////////////////////////////
# //
# //  Function Name : DisplayEven
# //  Description : It is used to print all even numbers till a given number
# //  Input :   Integer
# //  Ouput :   Void
# //  Author : Sakshi Pradeep Bhapkar
# //  Date : 19/1/2026
# //
# ///////////////////////////////////////////////////////////

def DisplayEven(No):
    for i in range(2,No+1):
        if (i%2 == 0):
            print(i,"\t",end="")


def main():
    DisplayEven(10)

if __name__ == "__main__":
    main()