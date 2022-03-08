import cv2 as cv
img = cv.imread("testeOpenCV.jpg")
# Retirando ROI (Region of Interest)
roi = img[50:150, 50:150]
cv.imshow("Joelma com ROI", roi)
cv.waitKey(0)
