import cv2
import numpy as np

# Creating our own image
img = np.zeros((512,512,3))

# Rectangle
cv2.rectangle(img,pt1=(100,100),pt2=(300,300),color=(255,0,0),thickness=1)

# Circle
cv2.circle(img,center=(100,400),radius=50,color=(0,0,255),thickness=1)

# Line
cv2.line(img,pt1=(0,0),pt2=(512,512),thickness=1,color=(0,255,0))

# Text
cv2.putText(img,org=(100,100),fontScale=4,color=(0,255,255),thickness=2,lineType=cv2.LINE_AA,text='Hello',fontFace=cv2.FONT_ITALIC)



cv2.imshow("Window",img)
cv2.waitKey(0)