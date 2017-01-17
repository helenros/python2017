def doblue(): print("The sea is blue")
def dogreen(): print("Grass is green")
def doyellow(): print("Sand is yellow")

def redflag():
   print("Red is the colour of fire")
   print("do NOT play with fire")

def errhandler ():
   print("Your input has not been recognised")

ColorSelect = {
 0: doblue,
 1: dogreen,
 2: doyellow
}

Selection = 0
while (Selection != 3):
 print("0. Blue")
 print("1. Green")
 print("2. Yellow")
 print("3. Quit")
 Selection = int(input("Select a color option: "))
 if (Selection >= 0) and (Selection < 3):
  ColorSelect[Selection]()
