import os

def main():
    FileName = input("Enter the name of file : ")

    Ret = os.path.exists(FileName)

    if (Ret == True) :
        print("File gets successfully opened")
        fobj = open(FileName,"r")
    else:
        print("There is no such file")
        

if __name__ == "__main__":
    main()
