##############################################################################################
#   Class name      :   Circle
#   Description     :   Class contains three instance variables and four instance methods
#                       Accept,CalculateArea,CalculateCircumferenceand Display
#                       and one class variable, to calcualte circle's area and circumference
#   Author          :   Sakshi Pradeep Bhapkar
#   Date            :   11/03/26
##############################################################################################

class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self, R):
        self.Radius = R
    
    def CalculateArea(self):
        self.Area = self.PI * self.Radius *self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * self.PI * self.Radius

    def Display(self):
        print(f"Radius of Circle is : {self.Radius}")
        print(f"Area of Circle is : {self.Area}")
        print(f"Circumference of the Circle is : {self.Circumference}")

    
def main():
    obj1 = Circle()
    obj2 = Circle()
    obj3 = Circle()

    obj1.Accept(2)
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

    obj2.Accept(4)
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.Display()

    obj3.Accept(5)
    obj3.CalculateArea()
    obj3.CalculateCircumference()
    obj3.Display()

if __name__ == "__main__":
    main()