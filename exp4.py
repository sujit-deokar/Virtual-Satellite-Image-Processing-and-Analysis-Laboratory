"""
============================
To genarate principle components of input raw image with general formats 
and also get inverse PCA with required number of principle components.
============================
created: 17/08/2015
auhor: sujitdeokar30@gmail.com
"""
import numpy as np
from sklearn.decomposition import PCA
from scipy import misc
import pylab as plt

X = misc.lena()
pca = PCA(n_components=50, whiten=False)
data = pca.fit_transform(X)
PCA(copy=True, n_components=2, whiten=False)
print(pca.explained_variance_ratio_) 
new_data = pca.inverse_transform(data)
shape(new_data)

plt.subplot(121)
plt.imshow(X)
plt.title('Orignal image')
plt.subplot(122)
plt.imshow(new_data)
plt.title('Reconstructed image')
plt.gray()
plt.show()
