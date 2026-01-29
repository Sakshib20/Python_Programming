import threading

# //////////////////////////////////////////////////////////////////
# //
# //  Function Name : Display1
# //  Description   : Displays the number from 1 to 50
# //  Input         : Nothing
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 29/1/2026
# //
# //////////////////////////////////////////////////////////////////

def Display1():
    print("1-50 : ")
    for i in range(1,51):
        print(i,end=" ")

# ////////////////////////////////////////////////////////////////////
# //
# //  Function Name : Display2
# //  Description   : Displays the number from 50 to 1
# //  Input         : Nothing
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 29/1/2026
# //
# ////////////////////////////////////////////////////////////////////

def Display2():
    print("\n50-1 : ")
    for i in range(50,0,-1):
        print(i,end=" ")

def main():
    t1 = threading.Thread(target=Display1)
    t2 = threading.Thread(target=Display2)

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("\nExit from main thread")

if __name__ == "__main__":
    main()

