#Convert 2 lists into a dictionary

#Using zip() and dict method

name=["a","b","c","d"]
marks=[100,99,98,98]

dictionary=zip(name,marks)
print(dict(dictionary))

# #Using zip() and list comprehension

# dictionary ={key:value for key,value in zip(name,marks)}
# print(dictionary)