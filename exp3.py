"""
============================
To smoothen the input raw satellite image or image with general formats using various 
smoothing filters such as average filter, Weighted average filter, Gaussian smoothing, etc.
============================
created: 17/08/2015
auhor: sujitdeokar30@gmail.com
"""
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
