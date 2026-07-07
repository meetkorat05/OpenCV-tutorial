import cv2
import numpy as np

image = cv2.imread("nature.jpeg")

# Gausian Blur

'''
blurred = cv2.GaussianBlur(image, (3,3), 3)
cv2.imshow("Original Image",image)
cv2.imshow("Blurred Image",blurred)
cv2.waitKey(0)
'''


# Median Blur

'''
blurred = cv2.medianBlur(image,11)
cv2.imshow("Original Image",image)
cv2.imshow("Blurred Image",blurred)
cv2.waitKey(0)
'''


# Sharpening Image

'''
sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharpened = cv2.filter2D(image, -1, sharpen_kernel)
cv2.imshow("Original Image",image)
cv2.imshow("Sharpened Image",sharpened)
cv2.waitKey(0)
'''