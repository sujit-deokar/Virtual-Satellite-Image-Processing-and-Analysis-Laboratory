-"""
-============================
-To Enhance the contrast of input raw satellite image or image with general fromats through various
-enhancement methods such as Linear Streching, enhancement using Standard Deviation, Histogram Equalization, etc.
-============================
-created: 17/08/2015
-auhor: sujitdeokar30@gmail.com
This code is taken and refurnish for our requirement from Open CV documents.
Please refer the http://docs.opencv.org/ site for additional details.
-"""
# Enhancement using Histogram Equalization:
import numpy as np
from scipy import misc
import pylab as plt
x = misc.lena()
hist,bins = np.histogram(x.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(x.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')
img2 = cdf[x]
plt.subplot(121)
plt.imshow(x)
plt.gray()
plt.title('original image')
plt.subplot(122)
plt.imshow(img2)
plt.gray()
plt.title('enhanced image')
plt.show()

'''
Alternative code for Histogram equalization based image enhancement.
Histograms Equalization in OpenCV OpenCV has a function to do this, cv2.equalizeHist(). 
Its input is just grayscale image and output is our histogram equalized image.
Below is a simple code snippet showing its usage for same image we used :
'''
import numpy as np
import cv2
from scipy import misc

img = misc.lena()
img = img.astype(np.uint8)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ))
cv2.imshow('img',img)
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
