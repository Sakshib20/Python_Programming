# ///////////////////////////////////////////////////////////
# //
# //  Function Name : DisplayFactors
# //  Description : It displays factors of a number
# //  Input :   Integer
# //  Ouput :   Void
# //  Author : Sakshi Pradeep Bhapkar
# //  Date : 19/1/2026
# //
# ///////////////////////////////////////////////////////////

def DisplayFactors(No):
    for i in range(1,No+1):
        if(No%i == 0):
            print(i,"\t",end="")


def main():
    DisplayFactors(12)

if __name__ == "__main__":
    main()