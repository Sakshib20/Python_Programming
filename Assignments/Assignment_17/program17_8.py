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
# Output =  1
#           1 2 
#           1 2 3
#           1 2 3 4
#           1 2 3 4 5

def Display(No):
    
    i = 1
    while(i != No+1):
        for j in range(1,i+1):
            print(j,"\t",end="")
        print()
        i=i+1


def main():
    Value = int(input("Enter number :"))

    Display(Value)
   

if __name__ == "__main__":
    main()

