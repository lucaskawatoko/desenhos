import cv2
import numpy as np

img = cv2.imread("coloque aqui o link da sua imagem")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 3 )
edges = cv2.adaptiveThreshold(gray, 9, cv2.ADAPTIVE_THRESH_MEAN_C,
                              cv2.THRESH_BINARY, 9, 9)

color = cv2.bilateralFilter(img, 9,100, 100)
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow("Image", img)
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()