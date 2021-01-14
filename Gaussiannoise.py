import cv2
import numpy as np
from matplotlib import pyplot as plt
# # Let's first create a zero image with the same dimensions of the loaded image
image = cv2.imread('C:\\Users\\Super\\Desktop\\opencv-python.png')
gaussian_noise = np.zeros((image.shape[0], image.shape[1]),dtype=np.uint8)
cv2.randn(gaussian_noise, 128, 20)
cv2.imshow('Gaussian noise',gaussian_noise)
cv2.waitKey()
cv2.imwrite("Gaussian random noise.jpg",gaussian_noise)
image = cv2.imread('C:\\Users\\Super\\Desktop\\opencv-python.png',cv2.IMREAD_GRAYSCALE)
gaussian_noise = (gaussian_noise*0.5).astype(np.uint8)
noisy_image1 = cv2.add(image,gaussian_noise)
cv2.imshow('Noisy image - Gaussian noise',noisy_image1)
cv2.waitKey()
cv2.imwrite("Noisy image1.jpg",noisy_image1)
blurred1 = cv2.medianBlur(noisy_image1, 3)
cv2.imshow('Median filter - Gaussian noise',blurred1)
cv2.waitKey()
cv2.imwrite("Median filter - Gaussian noise.jpg",blurred1)

