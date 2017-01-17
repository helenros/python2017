import sys
m1 = input("Enter Number of Rows for Matrix A :")
n1 = input("Enter Number of Columns for Matrix A :")

matA=[[0 for row in range(0,n1)] for col in range(0,m1)]

for i in range(m1):
         for j in range(n1):
             matA[i][j]=input()

m2 = input("Enter Number of Rows for Matrix B :")
n2 = input("Enter Number of Columns for Matrix B :")

matB=[[0 for row in range(0,n2)] for col in range(0,m2)]

for i in range(m2):
         for j in range(n2):
             matB[i][j]=input()

if (n1<>m2):
   print("Cannot perfomr Matrix Multiplication....")
   print("Since First Matrix Row and Second Matrix Column should be same")
   sys.exit()
else:
  matC=[[0 for row in range(0,m1)] for col in range(0,n2)]
  # multiply two matrices
for i in range(m1):
 for j in range(n2):
  matC[i][j] = 0
  for k in range(m2):
   matC[i][j] = matC[i][j] + matA[i][k] * matB[k][j]
  
print ("Matrix A  :  ")
for row in matA:
     print(row)

print ("Matrix B  :  ")
for row in matB:
     print(row)

print "Resultant matrix is: (matrixA * matrixB)"
for row in matC:
     print(row)
