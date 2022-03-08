import cv2 as cv
img = cv.imread("testeOpenCV.jpg")
#cv.imshow("Joelma", img)
#cv.waitKey(0)
print(img.size)
print(img.dtype)
# Número de linhas, colunas e canais (se for imagem colorida)
print(img.shape)
