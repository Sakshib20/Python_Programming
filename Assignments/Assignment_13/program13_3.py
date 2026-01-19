# ///////////////////////////////////////////////////////////
# //
# //  Function Name : ChkPerfect
# //  Description : It is used to check whether a number is perfect number or not
# //  Input :   Integer
# //  Ouput :   Boolean
# //  Author : Sakshi Pradeep Bhapkar
# //  Date : 19/1/2026
# //
# ///////////////////////////////////////////////////////////

def ChkPerfect(No):
    flag = False
    Sum = 0

    for i in range(1,(No//2)+1):
        if No%i == 0:
            Sum = Sum+i

    if Sum == No:
        flag = True

    return flag

def main():
    Ret = ChkPerfect(6)
    
    if Ret == True:
        print("Perfect Number")
    else:
        print("Not Perfect number")

if __name__ == "__main__":
    main()