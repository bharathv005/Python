#Find numbers divisible by another number

l=[39,48,26,33,98,67,97]
result= list(filter(lambda x: x%13==0,l))
print(result)

# num=int(input("Enter the number "))
# for i in range(1,101):
#     if i %num==0:
#         print(i)