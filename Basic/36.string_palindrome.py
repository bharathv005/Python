#Check given string is a palindrome

string=input("Enter a string ")
rev= string[::-1]
if(rev==string):
    print("Palindrome")
else:
    print("Not a palindrome")