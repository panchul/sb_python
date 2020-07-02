import cv2
import numpy as np

img = np.zeros((200,320,3),  # ! (height, width, colorspace)
               np.uint8)
cv2.imshow("the img", img)
cv2.waitKey(0)

img[:] = 255, 0, 0
cv2.imshow("whole blue", img)
cv2.waitKey(0)

img[40:80, 50:120] = 0, 0, 255
cv2.imshow("part red", img)
cv2.waitKey(0)
