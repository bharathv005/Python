#Simple calculator
import math
num1=float(input("Enter the number 1 "))
num2=float(input("Enter the number 2 "))
choice=input("Enter the operation ")

if choice=="+":
    print(num1+num2)
elif choice=="-":
    print(num1-num2)
elif choice=="*":
    print(num1*num2)
elif choice=="/":
    print(num1/num2)
elif choice=="^":
    print(num1**num2)
elif choice=="sqrt":
    print(math.sqrt(num1))
else:
    print("Enter valid operator")