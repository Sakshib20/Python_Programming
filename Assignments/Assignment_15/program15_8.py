# ///////////////////////////////////////////////////////////
# //
# //  Function Name : FDivByTF
# //  Description   : Used a filter function that accepts list of data and returns the numbers that are divisible by 3 and 5
# //  Input         : List
# //  Ouput         : List
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 21/1/2026
# //
# ///////////////////////////////////////////////////////////

FDivByTF = lambda No : No%3==0 and No%5==0 

def main():
    Data = [1,3,5,12,15,30]

    FData = list(filter(FDivByTF,Data))
    print(FData)

if __name__ == "__main__":
    main()

