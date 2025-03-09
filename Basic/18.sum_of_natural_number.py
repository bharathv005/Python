#Find the sum of natural numbers

num=int(input("Enter the natural number "))

if(num<=0):
    print("Enter a positive number ")
else:
    sum=0
    for i in range(1,num+1):
        sum+=i
    print(sum)