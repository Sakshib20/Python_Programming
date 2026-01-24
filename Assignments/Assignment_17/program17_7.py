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
# Output =  1 2 3 4 5
#           1 2 3 4 5
#           1 2 3 4 5
#           1 2 3 4 5
#           1 2 3 4 5

def Display(No):
    
    for i in range(1,No+1):
        for j in range(1,No+1):
            print(j,"\t",end="")
        print()
    
def main():
    Value = int(input("Enter number :"))

    Display(Value)
   

if __name__ == "__main__":
    main()

