
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
