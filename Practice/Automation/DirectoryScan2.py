import os

def DirectoryScanner(DirectoryName):

    print("Contents of the directory are : ")

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
        print("FolderName : ",FolderName)

        for subf in SubFolder:
            print("Subfolder name : ",subf)

        for fname in FileName:
            print("File Name : ",fname)

def main():
    DirectoryName = input("Enter name of directory : ")
    DirectoryScanner(DirectoryName)

if __name__=="__main__":
    main()