##############################################################################################
#   Class name      :   Bookstore
#   Description     :   Class contains two instance variables, one instance method as Display
#                       which displays name of author and number of books in total and one class
#                       variable as NoOfBooks. Whenever a new object is created the class variable
#                       is incremented by 1
#   Author          :   Sakshi Pradeep Bhapkar
#   Date            :   11/03/26
##############################################################################################

class Bookstore:
    NoOfBooks = 0

    def __init__(self,BName,BAuthor):
        self.Name = BName
        self.Author = BAuthor

        Bookstore.NoOfBooks = Bookstore.NoOfBooks + 1

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books : {Bookstore.NoOfBooks}")


def main():
    obj1 = Bookstore("Linux System Programming","Robert Love")
    obj1.Display()

    obj2 = Bookstore("C Programming","Dennis Ritchie")
    obj2.Display()

if __name__ == "__main__":
    main()
