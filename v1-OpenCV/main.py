import cv2
import numpy as np

img = cv2.imread("img/a_person_riding_a_bicycle_on_a_hill_with.jpeg")

image = cv2.resize(img,(512,512))

#img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#img_flip = cv2.flip(img_resize,-1)

#image_crop = img[0:300,0:300]

#cv2.imwrite('img_small.jpeg',image_crop)

cv2.imshow("Window",image)
cv2.waitKey(0)






