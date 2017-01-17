def openread(): 
      global fo
      print("File is opening in Read mode : ")
      fo = open("temp.txt", "r+")
      str = fo.read(10);
      print "Read String is : ", str
      with open("temp.txt", "r") as fin:
         print fin.read()
def openwrite(): 
      global fo
      print("File is opening in Write mode : ")
      fo = open("temp.txt", "w+")
      fo.write("hello world is tne new line written in the temp file")
      fo.write("and another line")
def getposition(): 
      global fo
      print("Gettting Current File pointer position : ")
      position = fo.tell();
      print "Current file position : ", position
def setatbegin():
      global fo
      print("Reposition the pointer at the beginning of the File : ")
      position = fo.seek(0, 0);
def errhandler ():
   print("Your input has not been recognised")

MenuSelect = {
 1: openread,
 2: openwrite,
 3: getposition,
 4: setatbegin
}

Selection = 0
while (Selection != 5):
 print("1. Open in Read Mode")
 print("2. Open in Write Mode")
 print("3. Current Position")
 print("4. Set at the Beginning")
 print("5. Quit")
 Selection = int(input("Select a Menu option: "))
 if (Selection >= 1) and (Selection < 5):
  MenuSelect[Selection]()
