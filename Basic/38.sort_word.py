# Sort Words in Aphabetic Order

string=input("Enter the string: ")

w=string.split()
 
for i in range(len(w)):
    w[i]=w[i].lower()

w.sort()

for i in range(len(w)):
    print(w[i],end=" ")