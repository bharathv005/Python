#Factorial of a number

#Using recursion
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return (n*fact(n-1))
   

num=int(input("Enter the number "))
r=fact(num)
print(r)

"""
#Using for loop
num=int(input("Enter the number "))
fact=1
if num=1:
    print("1")
else:
    for i in range(1,num+1):
        fact*=i
print(fact)
"""