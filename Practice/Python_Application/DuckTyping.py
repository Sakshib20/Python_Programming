# Duck Typing : it is a concept where the type of an object is determined :
# by it's behaviour, not by it's class

class InkjetPrinter:
    def printdocument(self, document):
        print("Inkjet printer printing : ",document)

class LaserPrinter:
    def printdocument(self, document):
        print("Laser printer printing : ",document)

class PDFWriter:
    def printdocument(self, document):
        print(f"Saving {document} as PDF")

def StarPrinting(Device):
    Device.printdocument("Marvellous notes")

def main():
    StarPrinting(InkjetPrinter())
    StarPrinting(LaserPrinter())
    StarPrinting(PDFWriter())


main()