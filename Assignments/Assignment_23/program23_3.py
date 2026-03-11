##############################################################################################
#   Class name      :   Numbers
#   Description     :   Class contains one instance variables and four instance methods as:
#                       ChkPrime()-    returns true if a number is Prime, 
#                       ChkPerfect()-  returns true if a number is Perfect,
#                       Factors()-     Displays all factors of a number,
#                       SumFactors() - returns the sum of all factors
#   Author          :   Sakshi Pradeep Bhapkar
#   Date            :   11/03/26
##############################################################################################

class Numbers:
    def __init__(self,no):
        self.Value = no
    
    def ChkPrime(self):
        for i in range(2,self.Value//2):
            if (self.Value%i==0):
                return False
            else:
                return True
   
    def ChkPerfect(self):

        Ret = self.SumFactors()

        if(Ret == self.Value):
            return True
        else:
            return False
   
    def Factors(self):
        print(f"Factors of {self.Value} are : ",end="")
        for i in range(1,self.Value//2):
            if (self.Value%i==0):
                print(i,end=" ")

        print()
        
    
    def SumFactors(self):
        Sum = 0
        for i in range(1,self.Value//2):
            if (self.Value%i==0):
                Sum = Sum + i

        return Sum

def main():
    obj1 = Numbers(12)

    print(obj1.ChkPrime())
    print("Sum of factors is : ",obj1.SumFactors())
    print(obj1.ChkPerfect())
    obj1.Factors()

    obj2 = Numbers(7)

    print(obj2.ChkPrime())
    print("Sum of factors is : ",obj2.SumFactors())
    print(obj2.ChkPerfect())
    obj2.Factors()

    obj3 = Numbers(8)

    print(obj3.ChkPrime())
    print("Sum of factors is : ",obj3.SumFactors())
    print(obj3.ChkPerfect())
    obj3.Factors()

if __name__ == "__main__":
    main()
