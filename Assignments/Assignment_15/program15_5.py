# ///////////////////////////////////////////////////////////
# //
# //  Function Name : RMax
# //  Description   : Used a reduce function that accepts list data and returns the maximum element 
# //  Ouput         : List
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 21/1/2026
# //
# ///////////////////////////////////////////////////////////
from functools import reduce

RMax = lambda No1,No2 : No1 if No1>No2 else No2

def main():
    Data = [1,2,13,4,5]

    RData = reduce(RMax,Data)
    print(RData)

if __name__ == "__main__":
    main()