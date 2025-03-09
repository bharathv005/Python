#Catch multiple exception in one line

string= input("Enter string ")

try:
    num=int(input("Enter a number "))
    print(string+num)
except(ValueError,TypeError) as a:
    print(a)