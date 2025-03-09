#Get the class name of a instance


#Using type() and __name__attributes

class SmartPhome:
    def name(self,name):
        return name

s1=SmartPhome()
print(type(s1).__name__)


# class SmartPhome:
#     def name(self,name):
#         return name

# s1=SmartPhome()
# print(s1/__class__.__name__)