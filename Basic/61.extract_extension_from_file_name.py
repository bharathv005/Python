#Extract extension from the file name

#Using os

import os

file_ext=os.path.splitext("C:/User/demo.py")
print(file_ext[1])

#Using pathlib module

from pathlib import Path

print(Path("C:/User/demo.py").suffix)