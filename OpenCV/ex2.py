# importe os pacotes necessários
import numpy as np
import cv2

# desenha um retângulo
rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)

# desenhar um círculo
circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)

# um bit a bit 'AND' só é 'Verdadeiro' quando ambas as entradas têm um valor que
# está 'ON' - neste caso, a função cv2.bitwise_and examina
# cada pixel no retângulo e círculo; se * AMBOS * pixels têm um
# valor maior que zero, então o pixel é ligado 'ON' (ou seja, 255)
# na imagem de saída; caso contrário, o valor de saída é definido como
# 'OFF' (i.e., 0)

bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

# um bit a bit 'OR' examina cada pixel nas duas entradas, e se
# * EITHER * pixel no retângulo ou círculo é maior que 0,
# então o pixel de saída tem um valor de 255, caso contrário, é 0

bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)