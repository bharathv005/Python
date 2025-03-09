#Display the powers of 2

num=int(input("Enter the number "))
result= list(map(lambda x: 2**x,range(num+1)))
print(result)


# l=[]
# for i in range(num+1):
#     l.append(2**i)

# print(l)