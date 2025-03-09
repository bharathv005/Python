#  Find the size(Resolution) of a image

import PIL
from PIL import Image

img = PIL.Image.open("C:/Users/img/image.png")  #Backword slashes to Forword slashes 

width,height = img.size

print(width,"x",height)  #Ex: 274 x 184