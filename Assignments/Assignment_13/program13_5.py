# ///////////////////////////////////////////////////////////
# //
# //  Function Name : DisplayGrade
# //  Description : It displays grade 
# //  Input :   Integer
# //  Ouput :   Void
# //  Author : Sakshi Pradeep Bhapkar
# //  Date : 19/1/2026
# //
# ///////////////////////////////////////////////////////////

def DisplayGrade(Marks):
    
    if Marks>=75:
        print("Distinction")

    if 75>Marks>=60:
        print("First Class")
    
    if 60>Marks>=50:
        print("Second Class")
    
    if Marks<50:
        print("Fail")
    

def main():
    DisplayGrade(45)

if __name__ == "__main__":
    main()