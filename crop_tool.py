import cv2
import numpy as np

img = cv2.imread("img/Muscle Car.jpg")

flag = False
ix = -1
iy = -1
def crop(event,x,y,flags,params):

    global flag,ix,iy

    if event == 1:
        flag = True
        ix = x
        iy = y

    elif event == 4:

        fx = x
        fy = y

        flag = False
        cv2.rectangle(img, pt1=(ix, iy), pt2=(x, y), thickness=1, color=(0, 0, 0))
        cropped = img[iy:fy,ix:fx]
        cv2.imshow("Window",cropped)
        cv2.waitKey(0)


cv2.namedWindow(winname="Window")
cv2.setMouseCallback("Window",crop)


while True:

    cv2.imshow("Window",img)

    if cv2.waitKey() & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()