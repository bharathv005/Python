#Compute the power of a number

#Using while loop

base=int(input("Enter base "))
expo=int(input("Enter exponent "))

res=1
while expo!=0:
    res=res*base
    expo=expo-1

print(res)

# #Using pow function

# x=pow(base,expo)
# print(x)