# -*- coding: utf-8 -*-
"""
Created on Sat Oct  4 14:16:06 2025

@author: Bhavya
"""

import numpy as np

x = [1, 2, 3]
h = [4, 5, 6]

linear_conv = np.convolve(x, h)
print("Linear Convolution: ", linear_conv) 

import numpy as np

x = [1, 2, 3]
h = [4, 5, 6]
N = max(len(x), len(h))
x_padded = np.pad(x, (0, N - len(x)), mode='constant')
h_padded = np.pad(h, (0, N - len(h)), mode='constant')
X_fft = np.fft.fft(x_padded)
H_fft = np.fft.fft(h_padded)
circular_conv = np.fft.ifft(X_fft * H_fft)
circular_conv = np.real(circular_conv)
print("Circular Convolution: ", circular_conv)


import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])

cross_corr = np.correlate(x, y, mode='full')

plt.stem(cross_corr)
plt.title('Cross-Correlation')
plt.show()


x = np.array([1, 2, 3, 4, 5])
auto_corr = np.correlate(x, x, mode='full')
plt.stem(auto_corr)
plt.title('Autocorrelation')
plt.show()



































