import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


img = mpimg.imread("images_tiger.png")

bw = img.mean(axis=2)
Hx = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1],
], dtype=np.float32)

Gx = convolve2d(bw, Hx)
plt.imshow(Gx, cmap='gray')

Gy = convolve2d(bw, Hx)
plt.imshow(Gy, cmap='gray')

G = np.sqrt(Gx * Gx + Gy * Gy)
plt.imshow(G, cmap='gray')
plt.show()