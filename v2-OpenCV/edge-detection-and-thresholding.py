import cv2
import numpy as np

image = cv2.imread("single-white-flower-main-focus-image.webp", cv2.IMREAD_GRAYSCALE)


# Canny

'''
edges = cv2.Canny(image, 50, 150)
cv2.imshow("Original Image",image)
cv2.imshow("Edges",edges)
cv2.waitKey(0)
'''


# Threshold

'''
ret, thresh_img = cv2.threshold(image,120,225,cv2.THRESH_BINARY)
cv2.imshow("Original Image",image)
cv2.imshow("Threshold Image",thresh_img)
cv2.waitKey(0)
'''


# BitWise Operation

'''
img1 = np.zeros((300,300), dtype="uint8")
img2 = np.zeros((300,300), dtype="uint8")

cv2.circle(img1, (150,150), 100, 255, -1)
cv2.rectangle(img2, (100,100), (250,250), 255, -1)

bitwise_and = cv2.bitwise_and(img1, img2)
bitwise_or = cv2.bitwise_or(img1, img2)
bitwise_not = cv2.bitwise_not(img1)

cv2.imshow("Circle", img1)
cv2.imshow("Rectangle", img2)
cv2.imshow("AND", bitwise_and)
cv2.imshow("OR", bitwise_or)
cv2.imshow("NOT", bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''



