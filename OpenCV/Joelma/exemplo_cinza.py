import cv2 as cv
img = cv.imread("testeOpenCV.jpg")
cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print(cinza.shape)
cv.imshow("Joelma Cinza", cinza)
cv.waitKey(0)
