import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("images_tiger.png")
bw = img.mean(axis=2)

W = np.zeros((20, 20))
for i in range(20):
    for j in range(20):
        dist = (i - 9.5) ** 2 + (j - 9.5) ** 2
        W[i, j] = np.exp(-dist / 50)

out = convolve2d(bw, W)

out3 = np.zeros(img.shape)
for i in range(3):
    out3[:, :, i] = convolve2d(img[:, :, i], W, mode="same")

plt.imshow(out3)
# plt.imshow(out, cmap='gray')
plt.show()
# out.shape()
# bw.shape()
