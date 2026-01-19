# ///////////////////////////////////////////////////////////
# //
# //  Function Name : ChkVowel
# //  Description : It is used to check whether a character is vowel or consonant
# //  Input :   String
# //  Ouput :   Boolean
# //  Author : Sakshi Pradeep Bhapkar
# //  Date : 19/1/2026
# //
# ///////////////////////////////////////////////////////////

def ChkVowel(cVal):
    flag = False

    if (cVal == 'a' or cVal== 'e' or cVal == 'i' or cVal == 'o' or cVal == 'u'):
        flag = True

    return flag

def main():
    Ret = ChkVowel('o')
    
    if Ret == True:
        print("Vowel")
    else:
        print("Consonant")

if __name__ == "__main__":
    main()