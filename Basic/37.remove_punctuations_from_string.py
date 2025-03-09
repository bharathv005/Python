#Remove punctuations from the given string
#Punctuations -> () {} - = _ , "" '' = ! <>

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

string = input("Enter anything:")

empty = ""
for i in string:
    if i not in punc:
        empty=empty+i

print(empty)