#Trim whitespace from a string

#Using strip function

string=" I like python "
print(string.strip())

# #Using regular expression

# import re
# string=" I like python "
# x=re.sub(r'^\s+|\s+$','',string)
# print(x)