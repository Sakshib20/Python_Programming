# ///////////////////////////////////////////////////////////
# //
# //  Function Name : FLengthCheck
# //  Description   : Used a filter function that accepts list of data and returns the even numbers from the list
# //  Input         : List
# //  Ouput         : List
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 21/1/2026
# //
# ///////////////////////////////////////////////////////////

FLengthCheck = lambda sValue : len(sValue)>5  

def main():
    Data = ["Apple","Jaguar","Car","Dog"]

    FData = list(filter(FLengthCheck,Data))
    print(FData)

if __name__ == "__main__":
    main()

