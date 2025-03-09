#Program to represent enum

from enum import Enum
class SmartPhone(Enum):
    Samsung = 1
    Nokia = 2
    Apple = 3

print(SmartPhone.Samsung.name)
print(SmartPhone.Samsung.value)