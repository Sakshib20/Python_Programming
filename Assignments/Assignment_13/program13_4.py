# ///////////////////////////////////////////////////////////
# //
# //  Function Name : DisplayBinary
# //  Description : It is used to display binary equivalent of a number
# //  Input :   Integer
# //  Ouput :   Void
# //  Author : Sakshi Pradeep Bhapkar
# //  Date : 19/1/2026
# //
# ///////////////////////////////////////////////////////////

def DisplayBinary(No):
    Sum = 0
    i=0
    while(i<4):
        if(No%2==0):
            if 2**i == No:
                print(1,end="")
            else:
                print(0,end="")
            i+=1
        else:
            if 2**i == No:
                print(1, end="")
                i += 1
            else:
                if Sum != No:
                    while(Sum != No):
                        Sum = Sum + 2**i
                        print(1, end="")
                        i += 1
                else:
                    print(0, end="") 
                    i+=1
                    
    
def main():
    
    DisplayBinary(5)

if __name__ == "__main__":
    main()