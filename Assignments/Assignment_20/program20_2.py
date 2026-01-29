import threading

# //////////////////////////////////////////////////////////////////
# //
# //  Function Name : EvenFactor
# //  Description   : Displays the sum of even factors of a number
# //  Input         : Integer
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 29/1/2026
# //
# //////////////////////////////////////////////////////////////////

def EvenFactor(No):
    Sum = 0

    for i in range(1,(No//2)+1):
        if(No%i)==0:
            if(i%2)==0:
                Sum = Sum+i

    print("Sum of Even factors is : ",Sum)

# ////////////////////////////////////////////////////////////////////
# //
# //  Function Name : OddFactor
# //  Description   : Displays the sum of odd factors of a number
# //  Input         : Integer
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 29/1/2026
# //
# ////////////////////////////////////////////////////////////////////

def OddFactor(No):
    Sum = 0

    for i in range(1,(No//2)+1):
        if(No%i)==0:
            if(i%2)!=0:
                Sum = Sum+i

    print("Sum of Odd factors is : ",Sum)

def main():
    t1 = threading.Thread(target=EvenFactor, args=(12,))
    t2 = threading.Thread(target=OddFactor, args= (12,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main thread")

if __name__ == "__main__":
    main()

