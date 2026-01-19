# ///////////////////////////////////////////////////////////
# //
# //  Function Name : Display
# //  Description : It displays the number from one to given number 
# //  Input :   Integer
# //  Ouput :   Void
# //  Author : Sakshi Pradeep Bhapkar
# //  Date : 19/1/2026
# //
# ///////////////////////////////////////////////////////////

def Display(No):
    for i in range(1,No+1):
        print(i,"\t",end="")
    

def main():
    Display(8)

if __name__ == "__main__":
    main()