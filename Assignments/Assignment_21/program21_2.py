import threading

# //////////////////////////////////////////////////////////////////
# //
# //  Function Name : Max
# //  Description   : Displays the maximum number from list
# //  Input         : Integer List
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 10/3/2026
# //
# //////////////////////////////////////////////////////////////////

def Max(data):
    iMax = data[0]

    for i in range(len(data)):
        if(data[i]>iMax):
            iMax = data[i]

    print("Maximum number is :",iMax)

# ////////////////////////////////////////////////////////////////////
# //
# //  Function Name : Min
# //  Description   : Displays the even number from the list
# //  Input         : Integer List
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 10/3/2026
# //
# ////////////////////////////////////////////////////////////////////

def Min(data):
    iMin = data[0]

    for i in range(len(data)):
        if(data[i]<iMin):
            iMin = data[i]

    print("Minimum number is :",iMin)

def main():

    Size = int(input("Enter number of elements : "))
    Data = list()

    for i in range(Size):
        Value = int(input())

        Data.append(Value)


    t1 = threading.Thread(target=Max, args=(Data,))
    t2 = threading.Thread(target=Min, args= (Data,))

    t1.start()
    t1.join()
    t2.start()
    
    t2.join()

    print("\nExit from main thread")

if __name__ == "__main__":
    main()

