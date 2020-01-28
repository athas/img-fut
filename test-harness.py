import imgfut

import imageio
import numpy as np

from matplotlib import pyplot as plt

mod = imgfut.imgfut()

img0 = np.array(imageio.imread('data/frog.png', pilmode='F'))

edges_img0 = mod.sobel_f32(img0)
blur_img0 = mod.mean_filter_f32(img0)

plt.gray()
plt.imshow(img0)
plt.show()
