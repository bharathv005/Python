#Check if a key is already present in a dictionary

friends ={"Rachel":"Ross","Monica":"Chandler","Phoebe":"Joe"}

name=input("Enter the key here ")

if name in friends.keys():
    print("Key is present ")
else:
    print("Key is not present")