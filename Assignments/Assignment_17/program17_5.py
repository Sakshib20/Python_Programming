# ///////////////////////////////////////////////////////////
# //
# //  Function Name : ChkPrime
# //  Description   : Checks if a number is prime or not
# //  Input         : Integer
# //  Ouput         : Boolean
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 24/1/2026
# //
# ///////////////////////////////////////////////////////////

def ChkPrime(No):
    bFlag = False

    for i in range(2,(No//2)+1):
        if(No%i==0):
            bFlag = True

    return bFlag

def main():
    Value = int(input("Enter number :"))

    Ret = ChkPrime(Value)

    if Ret == False:
        print("It is Prime number")

    else:
        print("Not a prime number")    

if __name__ == "__main__":
    main()

