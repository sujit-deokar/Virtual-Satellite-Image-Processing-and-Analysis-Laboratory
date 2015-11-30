"""
============================
To apply various Morphological operations, such as Erosion, Dilation, Boundary, Detection, Top-hat Transform, etc, 
on specific bands of input raw satellite image or image with general formats.
============================
created: 17/08/2015
auhor: sujitdeokar30@gmail.com
"""
from PIL import Image 
from scipy import misc, ndimage
import pylab as plt

'''
Binary closing operation using scipy.ndimage library code is referenced from scipy documentation
'''
a = np.zeros((5,5), dtype=np.int)
a[1:-1, 1:-1] = 1; a[2,2] = 0
print a
