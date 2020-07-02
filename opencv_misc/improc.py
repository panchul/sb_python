import cv2
import numpy as np

img = cv2.imread("sample.png")
print(f"img.shape is {img.shape}")

img = cv2.resize(img, ((int)(img.shape[1]/4), (int)(img.shape[0]/4)))
print(f"resized img.shape is {img.shape}")

imCropped = img[0:150, 200:300]
imGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imBlur = cv2.GaussianBlur(imGray, (7,7), 0)
imCanny = cv2.Canny(img, 150, 200)

mykernel = np.ones((5, 5), np.uint8)
imDilation = cv2.dilate(imCanny, mykernel, iterations=1)
imEroded = cv2.erode(imDilation, mykernel, iterations=1)

cv2.imshow("original", img)
cv2.imshow("original cropped", imCropped)
cv2.imshow("gray", imGray)
cv2.imshow("blur", imBlur)
cv2.imshow("canny", imCanny)
cv2.imshow("dilation(thickening)", imDilation)
cv2.imshow("eroded(thinning)", imEroded)

cv2.waitKey(0)  # forever
