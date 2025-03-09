#Print the fibonacci numbers


#using for loop
a=0
b=1
num=int(input("Enter the number "))
if num==1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(1,num+1):
        c=a+b
        a=b
        b=c
        print(c)




# def Fibonacci(n):

#     if n < 0:
#         print("Incorrect input")

#     elif n == 0:
#         return 0

#     elif n == 1 or n == 2:
#         return 1

#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)

# num=int(input("Enter the number "))
# print(Fibonacci(num))
