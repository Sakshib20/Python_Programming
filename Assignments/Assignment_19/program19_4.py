# //////////////////////////////////////////////////////////////
# //
# // Function Name : main
# // Description   : Accepts N numbers, filters the even numbers, 
# //                 calculates their square, and returns the addition of the modified values.
# // Input         : Integer (Size), List of Integers (Elements)
# // Output        : Integer (Final Product)
# // Author        : Sakshi Pradeep Bhapkar
# // Date          : 29/1/2026
# //
# //////////////////////////////////////////////////////////////

from functools import reduce

def main():
    Size = int(input("Enter Number of elements : "))
    LData = list()

    for i in range(Size):
        Value = int(input())
        LData.append(Value)

    print(f"Input List = {LData}")

    FData = list(filter((lambda No : No%2==0),LData))
    print(f"List after filter = {FData}")

    MData = list(map((lambda No : No**2),FData))
    print(f"List after map = {MData}")

    RData = reduce((lambda No1, No2 : No1+No2),MData)
    print(f"List after reduce = {RData}")
    
if __name__ == "__main__":
    main()

