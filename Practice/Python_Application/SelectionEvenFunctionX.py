#Procedural

def CheckEven(No):
    if(No%2 == 0):
        print("It is Even Number")
    else:
        print("It is Odd Number")

def main():
    Value = 0

    print("Enter the number : ")
    Value=int(input())

    CheckEven(Value)

if __name__ == "__main__":
    main()