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
