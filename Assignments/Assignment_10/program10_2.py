# ///////////////////////////////////////////////////////////
# //
# //  Function Name : DisplaySum 
# //  Description : It is used to print sum of 1st N natural numbers
# //  Input :   Integer
# //  Ouput :   Void
# //  Author : Sakshi Pradeep Bhapkar
# //  Date : 19/1/2026
# //
# ///////////////////////////////////////////////////////////

def DisplaySum(No):
    Sum = 0
    for i in range(1,No+1):
        Sum = Sum + i

    print(Sum)


def main():
    DisplaySum(5)

if __name__ == "__main__":
    main()