# ///////////////////////////////////////////////////////////
# //
# //  Module Name   : MarvellousNum
# //  Description   : It has 1 function named ChkPrime which return the prime number 
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 28/1/2026
# //
# ///////////////////////////////////////////////////////////

def ChkPrime(No):
    iCnt = 0
    for i in range(2,(No//2)+1):
        if(No%i)==0:
            iCnt+=1

    if iCnt == 0:
        return True
    else:
        return False