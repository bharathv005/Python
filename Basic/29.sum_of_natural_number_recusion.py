#Print the sum of natural number using recusion


def sumofnum(n):
    if n<=1:
        return 1
    else:
        return n+sumofnum(n-1)
    
num=int(input("Enter the number "))
print(sumofnum(num))