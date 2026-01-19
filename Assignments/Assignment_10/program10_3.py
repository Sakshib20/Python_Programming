# ///////////////////////////////////////////////////////////
# //
# //  Function Name : DisplayFact
# //  Description : It is used to print factorial of a number
# //  Input :   Integer
# //  Ouput :   Void
# //  Author : Sakshi Pradeep Bhapkar
# //  Date : 19/1/2026
# //
# ///////////////////////////////////////////////////////////

def DisplayFact(No):
    Fact = 1
    for i in range(1,No+1):
        Fact = Fact*i

    print(Fact)


def main():
    DisplayFact(5)

if __name__ == "__main__":
    main()