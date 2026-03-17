# sample input : python CommandLine3.py 10 11

import sys

def main():
    
    for i in range(len(sys.argv)):
        No1 = int(sys.argv[1])
        No2 = int(sys.argv[2])

        print(No1+No2)

if __name__ == "__main__":
    main()