import threading

# ///////////////////////////////////////////////////////////////////////////////////////
# //
# //  Function Name : EvenList
# //  Description   : Extracts even elements from the list and displays their sum
# //  Input         : List(Integer)
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 29/1/2026
# //
# ///////////////////////////////////////////////////////////////////////////////////////

def EvenList(*Numbers):
    Sum = 0

    for No in Numbers:
        if No%2==0:
            Sum = Sum+No

    print("Even List :",Sum)

# ///////////////////////////////////////////////////////////////////////////////////////
# //
# //  Function Name : OddList
# //  Description   : Extracts odd elements from the list and displays their sum
# //  Input         : List(Integer)
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 29/1/2026
# //
# ///////////////////////////////////////////////////////////////////////////////////////

def OddList(*Numbers):
    Sum = 0

    for No in Numbers:
        if No%2!=0:
            Sum = Sum+No

    print("Odd list :",Sum)

def main():
    t1 = threading.Thread(target=EvenList, args=(2,4,1,3))
    t2 = threading.Thread(target=OddList, args= (1,3,2,6))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main thread")

if __name__ == "__main__":
    main()

