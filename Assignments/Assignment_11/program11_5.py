# ///////////////////////////////////////////////////////////
# //
# //  Function Name : ChkPalindrome
# //  Description : Checks whether a number is palindrome or not
# //  Input :   Integer
# //  Ouput :   Boolean
# //  Author : Sakshi Pradeep Bhapkar
# //  Date : 19/1/2026
# //
# ///////////////////////////////////////////////////////////

def ChkPalindrome(No):
    CValue = No
    FValue = 0
    flag = False

    while(No!=0):
        digit = No%10
        FValue = (FValue*10)+digit
        No = No//10
        
    if CValue == FValue:
        flag = True

    return flag

def main():

    Ret = ChkPalindrome(121)

    if Ret == True:
        print("Palindrome")
    else:
        print("Not palindrome")


if __name__ == "__main__":
    main()