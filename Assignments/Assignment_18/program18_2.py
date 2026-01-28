# ///////////////////////////////////////////////////////////
# //
# //  Function Name : Max
# //  Description   : Returns the Maximum element from the list 
# //  Input         : List
# //  Ouput         : Integer
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 27/1/2026
# //
# ///////////////////////////////////////////////////////////

def Max(LData):
    maxValue = LData[0]
    for i in range(len(LData)):
        if LData[i]>maxValue:
            maxValue=LData[i]

    return maxValue
    
def main():
    Size = int(input("Enter the Number of elements :"))
    Data = list()

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ret = Max(Data)
    print("Maximum is :",Ret)

if __name__ == "__main__":
    main()

