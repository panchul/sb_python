import cv2
import numpy as np

img = cv2.imread("sample.png")
print(f"img.shape is {img.shape}")

width, height = 250, 350

#  those are manually looked-up, I used gimp.
pts1 = np.float32([[809, 939], [1026, 991], [784, 1306], [1028, 1295]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

mymatrix = cv2.getPerspectiveTransform(pts1, pts2)

imgOut = cv2.warpPerspective(img, mymatrix, (width, height))

cv2.imshow("img", img)
cv2.imshow("img2", imgOut)

#  do not write it right here, let the sample be under version control
#  cv2.imwrite("sample_warped.png", imgOut)

cv2.waitKey(0)  # forever
 