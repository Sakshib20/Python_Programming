# ///////////////////////////////////////////////////////////
# //
# //  Function Name : Add
# //  Description   : Returns addition of all elements from the list 
# //  Input         : List
# //  Ouput         : Integer
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 27/1/2026
# //
# ///////////////////////////////////////////////////////////

def Add(LData):
    Sum = 0
    for i in range(len(LData)):
        Sum = Sum+LData[i]

    return Sum
    
def main():
    Size = int(input("Enter the Number of elements :"))
    Data = list()

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ret = Add(Data)
    print("Addition of all elements is :",Ret)

if __name__ == "__main__":
    main()

