#Find if given number is armstrong number(153=>3 digits 1^3+5^3+3^3=153)

num=int(input("Enter the number "))

length=len(str(num))
temp=num
sum=0
while(temp>0):
    digit=temp%10
    sum+=digit**length
    temp=temp//10
if(num==sum):
    print("The given number is a Armstrong number")
else:
    print("The given number is not a Armstrong number")