# import complex math module
import cmath
import math

a = int(input("Enter the coefficients of a: "))
b = int(input("Enter the coefficients of b: "))
c = int(input("Enter the coefficients of c: "))

d = b**2-4*a*c # discriminant

if d < 0:
    print ("This equation has no real solution")
    x1 = (-b-cmath.sqrt(d))/(2*a)  
    x2 = (-b+cmath.sqrt(d))/(2*a)  
    print('The solution are {0} and {1}'.format(x1,x2))   
elif d == 0:
    x = (-b+math.sqrt(d))/2*a
    print (("This equation has one solutions: "), x)
else:
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)
    print ("This equation has two solutions: ", x1, " or", x2)


