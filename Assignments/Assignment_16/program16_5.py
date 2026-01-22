# ///////////////////////////////////////////////////////////
# //
# //  Function Name : Display
# //  Description   : Displays 10-1 in reverse order
# //  Input         : Void
# //  Ouput         : Void
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 22/1/2026
# //
# ///////////////////////////////////////////////////////////

def Display():
    for i in range(10,0,-1):
        print(i,"\t",end="")

def main():
    Display()

if __name__ == "__main__":
    main()

