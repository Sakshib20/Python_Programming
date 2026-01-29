import threading

# ///////////////////////////////////////////////////////////////////////////////////////
# //
# //  Function Name : Small
# //  Description   : Counts and displays the number of lowercase characters
# //  Input         : String
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 29/1/2026
# //
# ///////////////////////////////////////////////////////////////////////////////////////

def Small(Word):
    Sum = 0

    print("ID : ",threading.get_ident())
    print("NAME :",threading.current_thread().name)
    for letter in Word:
        if letter.islower():
            Sum += 1

    print("Number of lowercase characters are :",Sum)

# ///////////////////////////////////////////////////////////////////////////////////////
# //
# //  Function Name : Capital
# //  Description   : Counts and displays the number of uppercase characters
# //  Input         : String
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 29/1/2026
# //
# # ///////////////////////////////////////////////////////////////////////////////////////


def Capital(Word):
    Sum = 0

    print("ID : ",threading.get_ident())
    print("NAME :",threading.current_thread().name)
    
    for letter in Word:
        if letter.isupper():
            Sum += 1

    print("Number of Uppercase characters are :",Sum)
        
# ///////////////////////////////////////////////////////////////////////////////////////
# //
# //  Function Name : Digits
# //  Description   : Counts and displays the number of digits
# //  Input         : String
# //  Ouput         : Nothing
# //  Author        : Sakshi Pradeep Bhapkar
# //  Date          : 29/1/2026
# //
# # ///////////////////////////////////////////////////////////////////////////////////////


def Digits(Word):

    Sum = 0

    print("ID : ",threading.get_ident())
    print("NAME :",threading.current_thread().name)

    for letter in Word:
        if letter.isdigit():
            Sum += 1

    print("Number of Digits are :",Sum)


def main():
    t1 = threading.Thread(target=Small, args=("Sakshi123",))
    t2 = threading.Thread(target=Capital, args=("Sakshi123",))
    t3 = threading.Thread(target=Digits, args=("Sakshi123",))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Exit from main thread")



if __name__ == "__main__":
    main()

