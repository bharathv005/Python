#Find the factorial of given number using recursion

def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
    
num=int(input("Enter the number "))
print(fact(num))