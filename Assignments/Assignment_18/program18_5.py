# ///////////////////////////////////////////////////////////
# //
# //  Function Name : ListPrime
# //  Description   : Returns the addition of all prime numbers from the list 
# //  Input         : List
# //  Ouput         : Integer
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 28/1/2026
# //
# ///////////////////////////////////////////////////////////
import MarvellousNum  as mn

def ListPrime(LData):
    Sum = 0
    for i in range(len(LData)):
        Ret = mn.ChkPrime(LData[i])

        if Ret == True:
            Sum = Sum + LData[i]
    return Sum
    
def main():
    Size = int(input("Enter the Number of elements :"))
    Data = list()

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ret = ListPrime(Data)
    print(f"Addition is : {Ret} ")

if __name__ == "__main__":
    main()

