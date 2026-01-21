# ///////////////////////////////////////////////////////////
# //
# //  Function Name : FEven
# //  Description   : Used a filter function that accepts list of data and returns the even numbers from the list
# //  Input         : List
# //  Ouput         : List
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 21/1/2026
# //
# ///////////////////////////////////////////////////////////

FEven = lambda No : No%2==0

def main():
    Data = [1,2,3,4,5]

    FData = list(filter(FEven,Data))
    print(FData)

if __name__ == "__main__":
    main()

