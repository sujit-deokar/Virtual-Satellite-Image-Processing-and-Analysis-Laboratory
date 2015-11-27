"""
============================
To get Frequency spectrum of input raw satellite image or image with general formats, 
apply Gaussian and Butterworth filtering to the same.
============================
created: 17/08/2015
auhor: sujitdeokar30@gmail.com
"""
import numpy as np
import numpy.fft as fft
from scipy import misc, signal
import matplotlib.pyplot as plt

img = misc.lena()
w = signal.gaussian(50, 5.0)
fft_image = fft.fftshift(fft2(img))
real_fft = np.real(fft_image)
im2 = signal.sepfir2d(img, w, w)
fft_out = fft.fftshift(fft2(im2))
real_out_fft = np.real(fft_out)
plt.figure()
plt.subplot(121)
plt.plot(real_fft)
plt.title('FFT of original image')
plt.subplot(122)
plt.plot(real_out_fft)
plt.title('FFT of filtered image')
plt.show()
