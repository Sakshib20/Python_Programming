# ///////////////////////////////////////////////////////////
# //
# //  Function Name : DisplayBinary
# //  Description : It is used to display binary equivalent of a number
# //  Input :   Integer
# //  Ouput :   Void
# //  Author : Sakshi Pradeep Bhapkar
# //  Date : 05/03/2026
# //
# ///////////////////////////////////////////////////////////

def DisplayBinary(No):
    num = 0
    BiNum = list()
    
    while(No > 0):
        num = No%2
        BiNum.append(num)
        No = No//2

    for i in range(len(BiNum)-1,-1,-1):
        print(BiNum[i],end="")
                    
def main():
    
    DisplayBinary(6)

if __name__ == "__main__":
    main()