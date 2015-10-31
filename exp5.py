"""
============================
To genearate edge magnitude image from the corrosponding input raw satellite image or image 
with general formats through various edge operators such as Robert operator, Sobel operator, 
Perwitt operator, etc.
============================
created: 17/08/2015
auhor: sujitdeokar30@gmail.com
"""
from scipy import misc, signal
import numpy as np

x = misc.lena()
x1 = misc.lena().astype(np.float32)
'''
Please refer following site for basic understanding of Sobel filtering:
https://en.wikipedia.org/wiki/Sobel_operator 
'''
sobelx = np.array([[-1,0,1], [-2,0,2], [-1,0,1]], dtype=np.float32)
sobely = np.array([[1,2,1], [0,0,0], [-1,-2,-1]], dtype=np.float32)
im1 = signal.convolve2d(x1,sobelx,mode='same',boundary='symm')
im2 = signal.convolve2d(x1,sobely,mode='same',boundary='symm')
plt.imshow(x)
plt.title('Original image')
plt.figure()
plt.subplot(121)
plt.imshow(im1)
plt.title('Sobel opeartor in X direction image')
plt.gray()
plt.subplot(122)
plt.imshow(im2)
plt.title('Sobel operator in Y direction image')
plt.gray()
plt.show()

''' 
Please refer following site for basic understanding of Roberts filtering:
https://en.wikipedia.org/wiki/Roberts_cross  
'''
from scipy import misc, signal
import numpy as np

robertx = np.array([[1,0], [0,-1]], dtype=np.float32)
roberty = np.array([[0,1], [-1,0]], dtype=np.float32)
im3 = signal.convolve2d(x1,sobelx,mode='same',boundary='symm')
im4 = signal.convolve2d(x1,sobely,mode='same',boundary='symm')
im5 = sqrt(im3**2 + im4**2)
plt.figure()
plt.subplot(121)
plt.imshow(im3)
plt.title('Robert operator in X direction image')
plt.subplot(122)
plt.imshow(im4)
plt.title('Robert operator in Y direction image')
plt.gray()
plt.figure()
plt.imshow(im5)
plt.title('Roberts image')
plt.gray()
plt.show()
