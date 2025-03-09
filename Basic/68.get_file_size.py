#Obtain file size

import os
file_size = os.stat("C:/Users/Python")
print(file_size.st_size)