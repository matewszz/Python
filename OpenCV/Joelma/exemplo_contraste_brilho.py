import cv2 as cv
import numpy as np
img = cv.imread("testeOpenCV.jpg")
# Entre 1 e 3
alpha = 2.2
# Entre 0 e 100
beta = 50
new_image = np.zeros(img.shape, img.dtype)
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        for c in range(img.shape[2]):
            new_image[y, x, c] = np.clip(alpha*img[y, x, c] + beta, 0, 255)
cv.imshow('New Image', new_image)
cv.waitKey()
