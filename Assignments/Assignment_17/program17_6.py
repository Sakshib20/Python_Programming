# ///////////////////////////////////////////////////////////
# //
# //  Function Name : Display
# //  Description   : Displays the Pattern
# //  Input         : Integer
# //  Ouput         : Void
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 24/1/2026
# //
# ///////////////////////////////////////////////////////////

# Input  = 5
# Output =  * * * * *
#           * * * *
#           * * *
#           * *
#           *

def Display(No):
    
    i = No
    while(i != 0):
        for j in range(i):
            print("*\t",end="")
        print()
        i=i-1


def main():
    Value = int(input("Enter number :"))

    Display(Value)
   

if __name__ == "__main__":
    main()

