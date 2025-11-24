# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 13:33:34 2025

@author: Bhavya
"""
'''
import numpy as np
l1 = (1,2,3)
l2 = (4,5,6)
l3 = (7,8,9)
arr = np.array([l1,l2,l3])
print(arr)
print(arr[0:3,0])
print(arr[0,0:3])
print(arr[0,0]+arr[1,1]+arr[2,2])
'''

import numpy as np
from PIL import Image

img = Image.open(r"C:\Users\Bhavya\Desktop\PWP\MU.jpg")
#resized_img = img.resize((100,100))
#resized_img = img.resize((1024,800))
#resized_img.show()
img.show() #original

new_img = Image.new("RGB", (200,200), color = "blue") 
#(mode,dimension,colour)
new_img.show()

new_img = Image.new("L", (200,200), color = "white") #L-->grey scale
new_img.show()

##ARITHMETIC OPERATIONS

from PIL import Image,ImageChops
img1 = Image.open(r"C:\Users\Bhavya\Pictures\Priya\1.jpg")
img2 = Image.open(r"C:\Users\Bhavya\Pictures\Priya\2.jpg")
subtracted = ImageChops.subtract(img1,img2)
subtracted.show() 

added = ImageChops.add(img1,img2)
added.show()

img = Image.open(r"C:\Users\Bhavya\Desktop\PWP\MU.jpg")
gray = img.convert("L")
gray.show()

#black --> since same image
red, green, blue = img.split()
zeroed_band = red.point(lambda _: 0)
red_merge = Image.merge("RGB", (red, zeroed_band, zeroed_band))
green_merge = Image.merge("RGB", (zeroed_band, green, zeroed_band))
blue_merge = Image.merge("RGB", (zeroed_band, zeroed_band, blue))
red_merge.show()
green_merge.show()
blue_merge.show()
