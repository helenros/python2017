#Input an array of n numbers and find separately the sum of positive numbers and negative numbers

int_arr =list()

totnum=input("Enter how many elements you want : ")
print 'Enter the numbers in array : '

for i in range(int(totnum)):
  n=input("Number : ")
  int_arr.append(int(n))

print 'Entered Array : ', int_arr

pos_sum=0;
neg_sum=0;

for i in int_arr:
  if i>0:
      pos_sum=pos_sum + i;
  else:
      neg_sum=neg_sum + i;

print ("Sum of Positive numbers :  "+str(pos_sum))
print ("Sum of Negative numbers :  "+str(neg_sum))

