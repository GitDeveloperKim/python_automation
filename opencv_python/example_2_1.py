import cv2
from matplotlib import pyplot as plt

imageFile = './data/lena.jpg'
img = cv2.imread(imageFile)
img2 = cv2.imread(imageFile, 0)
cv2.imshow('Lena color', img)
cv2.imshow('Lena grayscale', img2)

cv2.waitKey()
cv2.destroyAllWindows()
