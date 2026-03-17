import os
def main():
    DirectoryName = input("Enter name of directory : ")

    print("Contents of the directory are : ")

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
        print("FolderName : ",FolderName)

        for subf in SubFolder:
            print("Subfolder name : ",subf)

        for fname in FileName:
            print("File Name : ",fname)

if __name__=="__main__":
    main()