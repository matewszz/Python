import cv2 as cv
img1 = cv.imread("testeOpenCV.jpg")
img2 = cv.imread("testeOpenCV2.png")
img1 = img1[0:150, 0:200]
img2 = img2[0:150, 0:200]
alpha = 0.5
beta = (1.0 - alpha)
blend = cv.addWeighted(img1, alpha, img2, beta, 0.0)
cv.imshow("Joelma com Linear Blend", blend)
cv.waitKey(0)
