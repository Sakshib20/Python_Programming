import sys

def main():
    Border = "-"*40
    print(Border)
    print("--------- Marvellous Automation --------")
    print(Border)

    if(len(sys.argv)==2):
        if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
            print("This Application is used to perform _________")
            print("This is a automation script")

        elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
            print("Use the given script as ")
            print("ScriptName.py Argument1 Argument2")
            print("Argument1 : _________")
            print("Argument2 : _________")
        else:
            print("Use the given flags as :")
            print("--u or --U : used to display the usage")
            print("--h or --H : used to display the help")
    else:
        print("Invalid number os command line arguments")
        print("Use the given flags as :")
        print("--u or --U : used to display the usage")
        print("--h or --H : used to display the help")

    print(Border)
    print("---- Thank you for using our script ----") 
    print("-------- Marvellous Infosystems --------")
    print(Border)
            
if __name__=="__main__":
    main()