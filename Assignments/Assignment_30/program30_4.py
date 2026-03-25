# //////////////////////////////////////////////////////////////////////////////////////
# //
# //  Function Name : CpyContents
# //  Description   : It accepts a 2 file name  from user(source file and destination file) 
#                     and copies content from one file to another
# //  Input         : String
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 25/3/2026
# //
# //////////////////////////////////////////////////////////////////////////////////////

def CpyContents(src,dest):
    fobj1 = open(src,'r')
    fobj2 = open(dest,"w")

    data = fobj1.read()
    fobj2.write(data)

    print(f"Contents of {src} copied into {dest}")
    
def main():
    src = input("Enter the name of Source File : ")
    dest = input("Enter the name of destination file : ")

    CpyContents(src,dest)

if __name__ == "__main__":
    main()