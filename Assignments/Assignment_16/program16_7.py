# ///////////////////////////////////////////////////////////
# //
# //  Function Name : ChkDiv
# //  Description   : Checks if a number if divisible by 5
# //  Input         : Integer
# //  Ouput         : Boolean
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 22/1/2026
# //
# ///////////////////////////////////////////////////////////

def ChkDiv(No):
    bFlag = False
    if No%5==0:
        bFlag = True
    
    return bFlag
       

def main():
    Num = int(input("Enter Number :"))
    Ret = ChkDiv(Num)

    print(Ret)

if __name__ == "__main__":
    main()

