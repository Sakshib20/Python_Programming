##############################################################################################
#   Class name      :   BankAccount
#   Description     :   Class contains two instance variables,one class variable as ROI and 
#                       three instance methods as:
#                       Display()- display account holder name, 
#                       Deposit()-accepts amount from user and adds it to balance,
#                       Withdraw()- accepts an amount from user and subtract it from balance,
#                       CalculateInterest() - calculates and returns interest
#   Author          :   Sakshi Pradeep Bhapkar
#   Date            :   11/03/26
##############################################################################################

class BankAccount:
    ROI = 10.5

    def __init__(self,a,b):
        self.Name = a
        self.Amount = b
    
    def Display(self):
        print(f"Account holder Name : {self.Name}\n Current Balance : {self.Amount}")

    def Deposit(self,Damt):
        self.Amount = self.Amount + Damt

    def Withdraw(self,Wamt):

        if(Wamt>self.Amount):
            print("Withdrawal is greater")
            return
        else:
            self.Amount = self.Amount-Wamt
    
    def CalculateInterest(self):
        Interest = (self.Amount + BankAccount.ROI)/100

        print(f"Rate of Interest is : {Interest}")

def main():
    obj1 = BankAccount("Sakshi",2000)

    obj1.Display()
    obj1.Deposit(1000)
    obj1.Display()
    obj1.Withdraw(5000)
    obj1.Display()
    obj1.CalculateInterest()

    obj2 = BankAccount("Krishna",5000)

    obj2.Display()
    obj2.Deposit(1000)
    obj2.Display()
    obj2.Withdraw(5000)
    obj2.Display()
    obj2.CalculateInterest()

if __name__ == "__main__":
    main()
