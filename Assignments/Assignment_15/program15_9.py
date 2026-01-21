# ///////////////////////////////////////////////////////////
# //
# //  Function Name : RMult
# //  Description   : Used a reduce function that accepts list data and returns multiplication of all elements from the list
# //  Input         : List
# //  Ouput         : List
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 21/1/2026
# //
# ///////////////////////////////////////////////////////////
from functools import reduce

RMult = lambda No1,No2 : No1*No2

def main():
    Data = [1,2,3,4,5]

    RData = reduce(RMult,Data)
    print(RData)

if __name__ == "__main__":
    main()