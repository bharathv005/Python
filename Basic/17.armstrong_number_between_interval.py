#Armstrong_number_between_interval

num1=int(input("Enter the starting number "))
num2=int(input("Enter the ending number "))

for i in range(num1,num2+1):
    temp=i
    sum=0
    lenth=len(str(i))
    while temp>0:
        digit=temp%10
        sum+=digit**lenth
        temp=temp//10
    if(sum==i):
        print(i)
        