import cv2 
import numpy as np
from scipy import ndimage

img_noisy1 = cv2.imread('./imagens_com_ruido/jetplane.png', 0) 
m, n = img_noisy1.shape 

kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])
highpass_3x3 = ndimage.convolve(img_noisy1, kernel)

gauss_highpass = img_noisy1 - highpass_3x3

cv2.imshow('image', gauss_highpass)
cv2.waitKey(0)
cv2.destroyAllWindows()