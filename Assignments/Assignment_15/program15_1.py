# ///////////////////////////////////////////////////////////
# //
# //  Function Name : MSquare
# //  Description   : Used a map function that accepts list of data and returns the square of each elements in a list
# //  Input         : List
# //  Ouput         : List
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 21/1/2026
# //
# ///////////////////////////////////////////////////////////

MSquare = lambda No : No**2

def main():
    Data = [1,2,3,4,5]

    MData = list(map(MSquare,Data))
    print(MData)

if __name__ == "__main__":
    main()

