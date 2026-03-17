def Display(A,B,C,D):
    print(A,B,C,D)

def main():
    # Display(10,20)  Not Allowedn- Less Arguments
    # Display(10,20,30,40,50) Not Allowed - Extra/More Arguments
    Display(10,20,30,40)  # ALoowed

if __name__ =="__main__":
    main()