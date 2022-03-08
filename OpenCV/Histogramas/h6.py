import dlib
import cv2

image = cv2.imread("../testeOpenCV.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hogFaceDetector = dlib.get_frontal_face_detector()
faces = hogFaceDetector(gray, 1)

for (i, rect) in enumerate(faces):
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Image", image)
k = cv2.waitKey()