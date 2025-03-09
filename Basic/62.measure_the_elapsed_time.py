#Measure the elapsed time

#Using time

import time

starting=time.time()
print("Hello world")

ending=time.time()
print(ending-starting)

# #Using timeit

# from timeit import default_timer as timer

# starting=timer()
# print("hello world")
# ending=timer()
# print(ending-starting)