# ///////////////////////////////////////////////////////////
# //
# //  Function Name : Display
# //  Description   : Displays first 10 even numbers on screen
# //  Input         : Integer
# //  Ouput         : Void
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 22/1/2026
# //
# ///////////////////////////////////////////////////////////

def Display():
    for i in range(2,21,2):
        print(i,"\t",end="")
       

def main():
    Display()

if __name__ == "__main__":
    main()

