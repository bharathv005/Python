#Find the hcf or gcd of given numbers

def findhcf(x,y):
    if(x>y):
        small=y
    else:
        small=x
    for i in range(1,small+1):
        if(x%i==0) and (y%i==0):
            hcf=i
    return hcf

num1=int(input("Enter 1st number "))
num2=int(input("Enter 2nd number "))
print("The hcf is",findhcf(num1,num2))