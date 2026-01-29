# //////////////////////////////////////////////////////////////
# //
# // Function Name : main
# // Description   : Accepts N numbers, filters the prime numbers, 
# //                 multiply each by 2, and returns the Maximum number from all modified values.
# // Input         : Integer (Size), List of Integers (Elements)
# // Output        : Integer (Final Product)
# // Author        : Sakshi Pradeep Bhapkar
# // Date          : 29/1/2026
# //
# //////////////////////////////////////////////////////////////

from functools import reduce

Prime = lambda No : No>1 and all(No%i != 0  for i in range(2,(No//2)+1))
Max = lambda No1, No2 : No1  if No1>No2 else No2

def main():
    Size = int(input("Enter Number of elements : "))
    LData = list()

    for i in range(Size):
        Value = int(input())
        LData.append(Value)

    print(f"Input List = {LData}")

    FData = list(filter(Prime,LData))
    print(f"List after filter = {FData}")

    MData = list(map((lambda No : No*2),FData))
    print(f"List after map = {MData}")

    RData = reduce(Max,MData)
    print(f"List after reduce = {RData}")
    
if __name__ == "__main__":
    main()

