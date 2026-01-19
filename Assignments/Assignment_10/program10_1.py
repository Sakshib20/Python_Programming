# ///////////////////////////////////////////////////////////
# //
# //  Function Name : DisplayTable 
# //  Description : It is used to print multiplication table of a number
# //  Input :   Integer
# //  Ouput :   Void
# //  Author : Sakshi Pradeep Bhapkar
# //  Date : 19/1/2026
# //
# ///////////////////////////////////////////////////////////

def DisplayTable(No):

    for i in range(1,11):
        print(No*i,"\t",end="")


def main():
    DisplayTable(4)

if __name__ == "__main__":
    main()