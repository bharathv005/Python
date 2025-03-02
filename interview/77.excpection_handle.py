#Exception handling

x=10

try:
    print(x/0)
except:
    print("Division of zero isnot possible ")
else:
    print("No error")
finally:
    print("Finally")