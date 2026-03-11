##############################################################################################
#   Class name      :   Demo
#   Description     :   Class contains two instance variables and two instance methods
#                       Fun() and Gun() and one class variable, to demonstrate oop in python
#   Author          :   Sakshi Pradeep Bhapkar
#   Date            :   11/03/26
##############################################################################################

class Demo:
    Value = 10

    def __init__(self,a,b):
        self.no1 = a
        self.no2 = b

    def Fun(self):
        print(f"Inside Fun Value of no1 is : {self.no1}, value of no2 is : {self.no2}")

    def Gun(self):
        print(f"Inside Gun Value of no1 is : {self.no1}, value of no2 is : {self.no2}")

    
def main():
    Obj1 = Demo(11, 21)
    Obj2 = Demo(51, 101)

    Obj1.Fun()
    Obj2.Fun()

    Obj1.Gun()
    Obj2.Gun()

if __name__ == "__main__":
    main()