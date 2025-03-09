#check if given is prime or not

num=int(input("Enter the number "))
count=0
for i in range(1,num):
    if(num%i==0):
        count=count+1
if(count==2):
    print("It is a prime")
else:
    print("It is not a prime")

"""
num=int(input("Enter the number "))
if num==1:
    print("It is not a prime")
if num>1:
    for i in range(2,num):
        if(num%i==0):
            print("It is not a prime")
            break
else:
    print("It is a prime")


"""