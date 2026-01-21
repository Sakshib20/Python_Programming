# ///////////////////////////////////////////////////////////
# //
# //  Function Name : FCountEven
# //  Description   : Used a filter function that accepts list of data and returns the count of even elements from the list
# //  Input         : List
# //  Ouput         : List
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 21/1/2026
# //
# ///////////////////////////////////////////////////////////

FCountEven = lambda No : No%2==0 

def main():
    Data = [1,3,5,12,15,30]

    FData = len(list(filter(FCountEven,Data)))
    print(FData)

if __name__ == "__main__":
    main()

