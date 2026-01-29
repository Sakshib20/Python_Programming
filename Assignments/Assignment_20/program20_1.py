import threading

# ///////////////////////////////////////////////////////////
# //
# //  Function Name : DisplayEven
# //  Description   : Display first 10 even numbers
# //  Input         : Nothing
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 29/1/2026
# //
# ///////////////////////////////////////////////////////////

def DisplayEven():
    print("\nEven numbers are : ")
    for i in range(2,21):
        if i%2==0:
            print(i,end=" ")

# ///////////////////////////////////////////////////////////
# //
# //  Function Name : DisplayOdd
# //  Description   : Display first 10 odd numbers
# //  Input         : Nothing
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 29/1/2026
# //
# ///////////////////////////////////////////////////////////

def DisplayOdd():
    print("\nOdd numbers are : ")
    for i in range(1,20):
        if i%2 != 0:
            print(i,end=" ")

def main():
    t1 = threading.Thread(target=DisplayEven)

    t2 = threading.Thread(target=DisplayOdd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()

