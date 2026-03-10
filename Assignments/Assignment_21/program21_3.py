import threading

iCnt = 0
lobj = threading.Lock()

# //////////////////////////////////////////////////////////////////
# //
# //  Function Name : Update
# //  Description   : Updates the value of variable
# //  Input         : Nothing
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 10/3/2026
# //
# //////////////////////////////////////////////////////////////////

def Update():
    global iCnt

    for _ in range(4):
        with lobj:
            iCnt = iCnt + 1

def main():
    global iCnt

    t1 = threading.Thread(target=Update())
    t2 = threading.Thread(target=Update())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Value of iCnt is :",iCnt)

if __name__ == "__main__":
    main()