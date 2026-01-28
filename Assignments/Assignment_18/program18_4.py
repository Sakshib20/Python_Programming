# ///////////////////////////////////////////////////////////
# //
# //  Function Name : CountFreq
# //  Description   : Returns the Minimum element from the list 
# //  Input         : List
# //  Ouput         : Integer
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 27/1/2026
# //
# ///////////////////////////////////////////////////////////

def CountFreq(LData, No):
    Cnt = 0
    for i in range(len(LData)):
        if LData[i]==No:
            Cnt+=1
    return Cnt
    
def main():
    Size = int(input("Enter the Number of elements :"))
    Data = list()

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Search = int(input("Enter element to search :"))

    Ret = CountFreq(Data,Search)
    print(f"Frequency of is {Search} is : {Ret} ")

if __name__ == "__main__":
    main()

