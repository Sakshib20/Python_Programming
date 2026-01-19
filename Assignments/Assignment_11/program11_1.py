# ///////////////////////////////////////////////////////////
# //
# //  Function Name : ChkPrime 
# //  Description : It is used to check whether a number is prime or not
# //  Input :   Integer
# //  Ouput :   Boolean
# //  Author : Sakshi Pradeep Bhapkar
# //  Date : 19/1/2026
# //
# ///////////////////////////////////////////////////////////

def ChkPrime(No):
    iCnt = 0
    flag = False

    for i in range(2,((No)//2)+1):
        if(No%i == 0):
            iCnt = iCnt+1

    if iCnt == 0:
        flag = True
    else:
        flag = False

    return flag

def main():
    Ret = ChkPrime(11)
    
    if Ret == True:
        print("It is prime")
    else:
        print("Not prime")

if __name__ == "__main__":
    main()