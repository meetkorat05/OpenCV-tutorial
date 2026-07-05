import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    cv2.imshow("Webcam",img_gray)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()