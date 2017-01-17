#Write a program to search an element using linear search
int_arr =list()

totnum=input("Enter how many elements you want : ")
print 'Enter the numbers in array : '

for i in range(int(totnum)):
  n=input("Number : ")
  int_arr.append(int(n))

print 'Entered Array : ', int_arr

key=input("Enter the key value to be searched :")

flag=-1
for i in int_arr:
    if i==key:
       pos=int_arr.index(i)
       flag=1
       break

if flag==1:
   print 'Key found at position : ' , pos+1
else:
   print 'Key not found'


