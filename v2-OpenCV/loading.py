import cv2

image = cv2.imread("Screenshot (374).png")

if image is None:
    print("Error: Image not Found")
else:
    print("Image loaded successfully.")