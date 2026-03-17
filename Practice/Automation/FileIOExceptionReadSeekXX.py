# seek(kuthe, kuthun)
# kuthun : 0/1/2
# 0:starting
# 1:current possition
#  2: end of file

def main():
    try:
        fobj = open("Hello.txt","r")
        print("File gets successfully opened")
         
        print("Current offset is : ",fobj.tell())       # 0

        fobj.seek(6,1)
        print("Current offset is : ",fobj.tell())       # 11

        Data = fobj.read(6)
        print("Data from file is : ",Data)

        print("Current offset is : ",fobj.tell())       # 17

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of application")
        

if __name__ == "__main__":
    main()