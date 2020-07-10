# Capturing images

import cv2
import numpy as np

capture = cv2.VideoCapture(0)
# you can set it to what you want, e.g.:
# cap = cv2.VideoCapture(0)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)

frame_width = int(capture.get(3))
frame_height = int(capture.get(4))
frame_index = 1

if capture.isOpened is False:
    print("error while opening the camera")

while capture.isOpened():

    # This is how to wrap around the video stream if needed:
    # frameCounter +=1
    # if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
    #    cap.set(cv2.CAP_PROP_POS_FRAMES,0)
    #     frameCounter=0
    # _, img = cap.read()
    
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
