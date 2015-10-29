
============================
**To smoothen the input raw satellite image or image with general formats using various 
smoothing filters such as average filter, Weighted average filter, Gaussian smoothing, etc.**
============================
created: 17/08/2015
*auhor: sujitdeokar30@gmail.com*

from scipy import misc, signal
import numpy as np

x = misc.lena()
x1 = misc.lena().astype(np.float32)
w = signal.gaussian(50, 5.0)
laplacian = np.array([[0,1,0], [1,-4,1], [0,1,0]], dtype=np.float32)
derfilt = np.array([1.0, -2, 1.0], dtype=np.float32)
ck = signal.cspline2d(x1, 8.0)
deriv = (signal.sepfir2d(ck, derfilt, [1]) + signal.sepfir2d(ck, [1], derfilt))
im1 = signal.convolve2d(x1,laplacian,mode='same',boundary='symm')
im2 = signal.sepfir2d(x, w, w) 
plt.subplot(221)
plt.imshow(x)
plt.title('original image')
plt.subplot(222)
plt.imshow(im1)
plt.title('laplacian filter image')
plt.subplot(223)
plt.imshow(im2)
plt.title('gaussian blurred iamge')
plt.subplot(224)
plt.imshow(deriv)
plt.gray()
plt.title('spline edge filter iamge')
plt.show()
''' 
**2D convolution is used for Image filtering in OpenCV.
As for one-dimensional signals, images also can be filtered with various low-pass filters (LPF), high-pass filters (HPF),
etc. A LPF helps in removing noise, or blurring the image. A HPF filters helps in finding edges in an image.
OpenCV provides a function, cv2.filter2D(), to convolve a kernel with an image. As an example, we will try 
anaveraging filter on an image. A 5x5 averaging filter kernel can be defined as follows:**

       | 1 1 1 1 1 |
    1  | 1 1 1 1 1 |
K = -  | 1 1 1 1 1 |
    25 | 1 1 1 1 1 |
       | 1 1 1 1 1 |
'''
import cv2
img = cv2.imread('opencv_logo.png')
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
plt.figure()
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

''' 
**Image blurring can also be achieved using OpenCV function of *cv2.blur*. Here Kernel element is taken as
input and taken care inside the function itself.**
'''
import cv2
import numpy as np
import pylab as plt
from scipy import misc

x = misc.lena()
x = x.astype(np.uint8)
blur = cv2.GaussianBlur(x,(9,9),50)
blur1 = cv2.blur(x,(9,9))
plt.subplot(1,3,1)
plt.imshow(x)
plt.title('Original Image')
plt.subplot(1,3,2)
plt.imshow(blur)
plt.title('Image blurring using *cv2.blur* function in an Image')
plt.subplot(1,3,3)
plt.imshow(blur1)
plt.title('Image blurring using *cv2.GaussianBlur* function in an Image')
plt.gray()
plt.show()
