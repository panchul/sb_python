import cv2
import numpy as np

img = np.zeros((200, 320, 3),  # ! (height, width, colorspace)
               np.uint8)
cv2.imshow("the img", img)
cv2.waitKey(0)

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.imshow("line", img)
cv2.waitKey(0)

cv2.rectangle(img, (20, 40), (img.shape[1], img.shape[0]), (0, 255, 255),
              3)  # or cv2.FILLED to fill
cv2.imshow("rectangle", img)
cv2.waitKey(0)

cv2.circle(img, (90, 90), 60, (0, 0, 255), 5)
cv2.imshow("circle", img)
cv2.waitKey(0)

cv2.putText(img, "something", org=(90, 90), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1,
            color=(250, 0, 250), thickness=1)
cv2.imshow("text", img)
cv2.waitKey(0)
