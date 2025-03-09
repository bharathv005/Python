#two strings are anagram

s1=input("Enter string 1 ")
s2=input("Enter string 2 ")

if len(s1)==len(s2):
    a1=sorted(s1)
    a2=sorted(s2)
    if(a1==a2):
        print("It is Anagram")
    else:
        print("Not a Anagram ")
else:
    print("Not a Anagram ")