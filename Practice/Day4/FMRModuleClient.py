from MarvellousFMR import filterX,mapX,reduceX

CheckEven = lambda No: No%2==0
Increment = lambda No : No+1
Add = lambda A,B : A+B

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is :",Data)

    FData = list(filterX(CheckEven,Data))
    print("Data After Filter is :",FData)

    MData = list(mapX(Increment,FData))
    print("Data After map is :",MData)

    RData = reduceX(Add,MData)
    print("Data After reduce is :",RData)

    print(filterX)

if __name__ == "__main__":
    main()