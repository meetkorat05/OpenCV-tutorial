import cv2
import numpy as np

def draw(event,x,y,flags,params):
    if event == 1:
        cv2.circle(img,center=(x,y),radius=50,color=(0,0,255),thickness=-1)

cv2.namedWindow(winname="Window")
cv2.setMouseCallback("Window",draw)



img = np.zeros((512,512,3))

while True:

    cv2.imshow("Window",img)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()