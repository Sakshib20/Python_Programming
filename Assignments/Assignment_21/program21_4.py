import threading

# //////////////////////////////////////////////////////////////////
# //
# //  Function Name : Sum
# //  Description   : Displays the Sum of all elements from list
# //  Input         : Integer List
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 10/3/2026
# //
# //////////////////////////////////////////////////////////////////

def Sum(Data):
    iSum = 0

    for i in range(len(Data)):
        iSum = iSum + Data[i]

    print("Sum of all elements is : ",iSum)  

# //////////////////////////////////////////////////////////////////
# //
# //  Function Name : Prod
# //  Description   : Displays the Product of all elements from list
# //  Input         : Integer List
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 10/3/2026
# //
# ////////////////////////////////////////////////////////////////// 

def Prod(data):
    iProd = 1

    for i in range(len(data)):
        iProd = iProd * data[i]      

    print("Multiplication of all the elements is : ",iProd)          

def main():
    size = int(input("Enter number of elements : "))

    Data = list()
    elem = 0

    for i in range(size):
        elem = int(input("Enter Number : "))
        Data.append(elem)

    t1 = threading.Thread(target=Sum,args=(Data,))
    t2 = threading.Thread(target=Prod,args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()