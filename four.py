
#Recursive function for binary search
def binary_search(the_array, the_key, imin, imax):
    if (imax < imin):
        return -1
    else:
        imid = imin + ((imax - imin) / 2)
        if the_array[imid] > the_key:
            return binary_search(the_array, the_key, imin, imid-1)
        elif the_array[imid] < the_key:
            return binary_search(the_array, the_key, imid+1, imax)
        else:
            return imid
	

int_arr =list()
totnum=input("Enter how many elements you want : ")
print 'Enter the numbers in ascending order : '

for i in range(int(totnum)):
  n=input("Number : ")
  int_arr.append(int(n))


the_key=input("Enter the key value to be searched :")
print 'Entered Array : ', int_arr

# Function call
result=-1
result = binary_search(int_arr, the_key, 0 ,len(int_arr)-1)

if result!=-1:
    print ("Element is present at index : "+str(result+1))
else:
    print "Element is not present in array"


