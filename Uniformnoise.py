import cv2
import numpy as np
from matplotlib import pyplot as plt
# # Let's first create a zero image with the same dimensions of the loaded image
image = cv2.imread('C:\\Users\\Super\\Desktop\\Free-Wallpaper-downloads-2.jpg')
uniform_noise = np.zeros((image.shape[0], image.shape[1]),dtype=np.uint8)
cv2.randu(uniform_noise,0,255)
cv2.imshow('Uniform random noise',uniform_noise)
cv2.waitKey()
cv2.imwrite("Uniform random noise.jpg",uniform_noise)
image = cv2.imread('C:\\Users\\Super\\Desktop\\Free-Wallpaper-downloads-2.jpg',cv2.IMREAD_GRAYSCALE)
uniform_noise = (uniform_noise*0.5).astype(np.uint8)
noisy_image2 = cv2.add(image,uniform_noise)
cv2.imshow('Noisy image - Uniform noise',noisy_image2)
cv2.waitKey()
cv2.imwrite("Noisy image2.jpg",noisy_image2)
blurred2 = cv2.medianBlur(noisy_image2, 3)
cv2.imshow('Median filter - Uniform noise',blurred2)
cv2.waitKey()
cv2.imwrite("Median filter - Uniform noise.jpg",blurred2)