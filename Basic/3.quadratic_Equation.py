#Solve Quadratic Equation (ax**2+bx+c)
#a,b,c are real numbers
#a!=0

import cmath

a= int(input("Enter a(a!=0): "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))

d= (b**2)-(4*a*c)
root1 = (-b-cmath.sqrt(d))/(2*a)
root2 = (-b+cmath.sqrt(d))/(2*a)

print("The roots are",root1,"and",root2)