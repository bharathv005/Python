#Find the largest among 3 numbers

num1=int(input("Enter the 1st number "))
num2=int(input("Enter the 2nd number "))
num3=int(input("Enter the 3rd number "))
if(num1>num2 and num1>num3):
    print(num1,"is the greatest")
elif(num2>num1 and num2>num3):
    print(num2,"is the greatest")
else:
    print(num3,"is the greatest")