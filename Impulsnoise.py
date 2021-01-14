import cv2
import numpy as np
from matplotlib import pyplot as plt
# # Let's first create a zero image with the same dimensions of the loaded image
image = cv2.imread('C:\\Users\\Super\\Desktop\\Free-Wallpaper-downloads-2.jpg')
uniform_noise = np.zeros((image.shape[0], image.shape[1]),dtype=np.uint8)
cv2.randu(uniform_noise,0,255)
impulse_noise = uniform_noise.copy()
ret,impulse_noise = cv2.threshold(uniform_noise,250,255,cv2.THRESH_BINARY)
cv2.imshow('Impuls noise',impulse_noise)
cv2.waitKey()
cv2.imwrite("Impuls noise.jpg",impulse_noise)
image = cv2.imread('C:\\Users\\Super\\Desktop\\Free-Wallpaper-downloads-2.jpg',cv2.IMREAD_GRAYSCALE)
impulse_noise = (impulse_noise*0.5).astype(np.uint8)
noisy_image3 = cv2.add(image,impulse_noise)

cv2.imshow('Noisy image - Impuls noise',noisy_image3)
cv2.waitKey()
cv2.imwrite("Noisy image3.jpg",noisy_image3)
blurred3 = cv2.medianBlur(noisy_image3, 3)
cv2.imshow('Median filter - Impuls noise',blurred3)
cv2.waitKey()
cv2.imwrite("Median filter - Impuls noise.jpg",blurred3)