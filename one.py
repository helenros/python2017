#prg to print sum of n1 to n2

n1 = input("Enter n1 :")
n2 = input("Enter n2 :")

sum=0
i=n1

while i<=n2 :
  sum = sum+i
  i=i+1

print ("Sum of Numbers from "+str(n1)+" to "+str(n2)+" = "+str(sum))



