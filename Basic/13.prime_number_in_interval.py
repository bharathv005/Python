#All prime Numbers in a Interval

num1=int(input("Enter the starting number "))
num2=int(input("Enter the end number "))
for i in range(num1,num2+1):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count=count+1
    if(count==2):
        print(i)


"""

num1=int(input("Enter the starting number "))
num2=int(input("Enter the end number "))
for i in range(num1,num2+1):
    if i>1:
        for j in range(2,i):
            if(i%j==0):
            break
    else:
        print(i)
"""