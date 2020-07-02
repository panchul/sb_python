# Capturing images

import cv2
import numpy as np

capture = cv2.VideoCapture(0)
frame_width = int(capture.get(3))
frame_height = int(capture.get(4))
frame_index = 1

if capture.isOpened is False:
    print("error while opening the camera")

while capture.isOpened():
    ret, frame = capture.read()
    if ret is True:
        cv2.imshow("input frame", frame)
        # grayframe=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # cv2.imshow("gray frame",grayframe)

        mykey = cv2.waitKey(10) & 0xFF
        if mykey == ord('c'):
            framename = "camera_frame{}.png".format(frame_index)
            cv2.imwrite(framename, frame)
            frame_index = frame_index+1
        else:
            if mykey == ord('q'):
                break
    else:
        break

capture.release()
cv2.destroyAllWindows()
