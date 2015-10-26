
"""
============================
To view single band or color composite image. Subset image and its pixel data of raw satellite image
or general image formats with image histogram.
============================

created: 17/08/2015
auhor: sujitdeokar30@gmail.com
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2

Color_image = cv2.imread('sample.jpg')

b,g,r = cv2.split(Color_image)      
New_color_image = cv2.merge([r,g,b])     

plt.imshow(Color_image)
plt.show()

plt.imshow(b)
plt.show()

plt.imshow(New_color_image)
plt.show()

color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([Color_image],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()

''' Other way for separating the images'''

import numpy as np
import cv2
# Load an color image in grayscale
img = cv2.imread('test.png')
img1 = img[:,:,0]  #Red component
img2 = img[:,:,1]  #Green component
img3 = img[:,:,2]  #Blue component
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.imshow('image',img0)
cv2.waitKey(0)
cv2.imshow('image',img1)
cv2.waitKey(0)
cv2.imshow('image',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
