#Read a file line by line into a list

#loop and list
f=open("file.txt","r")
line=[line for line in f]
print(line)
new_lines=[x.strip() for x in line]
print(new_lines)

# #Using readlines()
# f=open("file.txt","r")
# lines=f.readlines()

# new_lines=[x.strip() for x in lines]
# print(new_lines)