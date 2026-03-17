class Arithmetic:
    def Addition(self,a,b):
        return a+b

    def Substraction(self,a,b):
        return a-b

No1 = 0
No2 = 0
Ans = 0

No1 = int(input("Enter 1st number :"))
No2 = int(input("Enter 2nd number :"))

Ans = Arithmetic().Addition(No1,No2)
print("Addition is : ",Ans)

Ans = Arithmetic().Substraction(No1,No2) 
print("Subtraction is : ",Ans)