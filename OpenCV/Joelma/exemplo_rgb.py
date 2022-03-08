import cv2 as cv
img = cv.imread("testeOpenCV.jpg")

# Acessando um pixel individual
(B, G, R) = img[50, 50]
print("R={}, G={}, B={}".format(R, G, B))

# Acessando somente o canal azul
azul = img[50, 50, 0]
print("Azul={}".format(azul))

# Modificando um pixel individual
img[50, 50] = [255, 0, 0]
img[50, 51] = [255, 0, 0]
img[51, 50] = [255, 0, 0]
img[51, 51] = [255, 0, 0]
cv.imshow("Joelma com RGB", img)
cv.waitKey(0)
