import cv2

image = cv2.imread("new_output.png")


# Resizing Image
'''
resized_image = cv2.resize(image,(960,540))
cv2.imshow("Resized Image",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''


# Cropping Image using Slicing
'''
cropped = image[100:200,50:150]
cv2.imshow("Cropped_image",cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''


# Image rotation
'''
(h,w) = image.shape[:2]
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated = cv2.warpAffine(image,M,(w,h))
cv2.imshow("Rotated Image", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''


# Image flipping
'''
flipped_horizontal = cv2.flip(image,1)
flipped_vertical = cv2.flip(image,0)
flipped_both = cv2.flip(image,-1)

cv2.imshow("Original",image)
cv2.imshow("Flipped Horizontal",flipped_horizontal)
cv2.imshow("Flipped Vertical",flipped_vertical)
cv2.imshow("Flipped Both",flipped_both)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''


# Drawing Shapes

'''
pt1 = (50,100)
pt2 = (300,100)
color = (255,0,0)
thickness = 2

cv2.line(image,pt1,pt2,color,thickness)
cv2.imshow("Line Example", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
cv2.rectangle(image,(100,100),(600,500),(0,0,255),3)
cv2.imshow("Rectangle Example",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
cv2.circle(image,(350,300),200,(0,255,0),2)
cv2.imshow("Circle Example",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
cv2.putText(image,"WLGYT",(285,150),
            cv2.FONT_HERSHEY_SIMPLEX,1.2,(0,0,255),2)
cv2.imshow("Font Example",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

