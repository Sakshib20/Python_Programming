import threading

# //////////////////////////////////////////////////////////////////
# //
# //  Function Name : Prime
# //  Description   : Displays the sum of even factors of a number
# //  Input         : Integer
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 29/1/2026
# //
# //////////////////////////////////////////////////////////////////

def Prime(Data):
    Sum = 0
    print("\nPrime Numbers Are : ")
    for i in range(len(Data)):
        for j in range(2,(Data[i]//2)+1):
            if(Data[i]%j)==0:
                Sum = Sum+1

        if Sum==0:
            print(Data[i],end="\t")

# ////////////////////////////////////////////////////////////////////
# //
# //  Function Name : NonPrime
# //  Description   : Displays the sum of odd factors of a number
# //  Input         : Integer
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 29/1/2026
# //
# ////////////////////////////////////////////////////////////////////

def NonPrime(Data):
    Sum = 0
    print("\nNon Prime Numbers Are : ")
    for i in range(len(Data)):
        for j in range(2,(Data[i]//2)+1):
            if(Data[i]%j)==0:
                Sum = Sum+1

        if Sum>0:
            print(Data[i],end="\t")

def main():

    Size = int(input("Enter number of elements : "))
    Data = list()

    for i in range(Size):
        Value = int(input())

        Data.append(Value)


    t1 = threading.Thread(target=Prime, args=(Data,))
    t2 = threading.Thread(target=NonPrime, args= (Data,))

    t1.start()
    t1.join()
    t2.start()
    
    t2.join()

    print("\nExit from main thread")

if __name__ == "__main__":
    main()

