
##############################################################################################
#   Class name      :   Arithematic
#   Description     :   Class contains two instance variables and five instance methods
#                       Accept, Addition, Subtraction, Multplication, Division and 
#                       one class variable, to perform basic Arithmetic operations
#   Author          :   Sakshi Pradeep Bhapkar
#   Date            :   11/03/26
##############################################################################################
class Arithematic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self,no1,no2):
        self.Value1 = no1
        self.Value2 = no2
    
    def Addition(self):
        print("Addition is : ",self.Value1+self.Value2)
    
    def Subtraction(self):
        print( "Subtraction is : ",self.Value1-self.Value2)
    
    def Multiplication(self):
        print("Multiplication is : ",self.Value1*self.Value2)
    
    def Division(self):
        print("Division is : ",self.Value1/self.Value2)
    

def main():
    obj1 = Arithematic()
    obj2 = Arithematic()

    obj1.Accept(12,11)
    obj1.Addition()
    obj1.Subtraction()
    obj1.Multiplication()
    obj1.Division()

    obj2.Accept(14,4)
    obj2.Addition()
    obj2.Subtraction()
    obj2.Multiplication()
    obj2.Division()   

if __name__ == "__main__":
    main()