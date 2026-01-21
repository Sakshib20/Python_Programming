# ///////////////////////////////////////////////////////////
# //
# //  Function Name : RAdd
# //  Description   : Used a reduce function that accepts list data and returns addition of all elements from the list
# //  Input         : List
# //  Ouput         : List
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 21/1/2026
# //
# ///////////////////////////////////////////////////////////
from functools import reduce

RAdd = lambda No1,No2 : No1+No2

def main():
    Data = [1,2,3,4,5]

    RData = reduce(RAdd,Data)
    print(RData)

if __name__ == "__main__":
    main()