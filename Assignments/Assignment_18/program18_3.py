# ///////////////////////////////////////////////////////////
# //
# //  Function Name : Min
# //  Description   : Returns the Minimum element from the list 
# //  Input         : List
# //  Ouput         : Integer
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 27/1/2026
# //
# ///////////////////////////////////////////////////////////

def Min(LData):
    minValue = LData[0]
    for i in range(len(LData)):
        if LData[i]<minValue:
            minValue=LData[i]

    return minValue
    
def main():
    Size = int(input("Enter the Number of elements :"))
    Data = list()

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ret = Min(Data)
    print("Minimum is :",Ret)

if __name__ == "__main__":
    main()

