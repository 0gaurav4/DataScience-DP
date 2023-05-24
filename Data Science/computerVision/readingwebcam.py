import cv2

img = cv2.imread("ppt.jpg", 1)

# print(img)

cv2.imshow('Image Viewer', img)
cv2.waitKey(5000)