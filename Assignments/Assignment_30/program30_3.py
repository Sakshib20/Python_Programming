# //////////////////////////////////////////////////////////////////////////////////////
# //
# //  Function Name : Display
# //  Description   : It accepts a file name  from user and 
#                     displays content of file line by line in screen
# //  Input         : String
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 25/3/2026
# //
# //////////////////////////////////////////////////////////////////////////////////////

def Display(fName):
    fobj = open(fName,'r')
    iCnt = 0

    data = fobj.read()

    for line in data:
        print(line.strip())
    
def main():
    fName = input("Enter name of File : ")

    Display(fName)

if __name__ == "__main__":
    main()