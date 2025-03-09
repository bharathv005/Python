# Count number of each vowel

#Using Dictionary

a=input("Enter the sentance ")
a=a.casefold()
vowels="aeiou"

count={}.fromkeys(vowels,0)

for char in a:
    if char in count:
        count[char]+=1

print(count)

# #Using List and dictionary comprehen

# a=input("Enter the sentance ")
# a=a.casefold()
# vowels="aeiou"

# count={key:sum([1 for char in a if char == key]) for key in vowels}
# print(count)


