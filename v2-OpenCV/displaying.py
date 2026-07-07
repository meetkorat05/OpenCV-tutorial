import cv2

# Displaying the Image

image = cv2.imread("Screenshot (374).png")

'''
if image is not None:
    cv2.imshow("Image Showing",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Could not load the image")
'''

# Saving the Edited Image

'''
cv2.imwrite("output.png",image)
'''

# Image Shape

'''
print(image.shape)
'''

# Convert color of the Image

'''
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''