import cv2
import numpy as np

def do_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 50, (0,0,255), -1)

img = cv2.imread("sample.png")
#img = np.zeros((600, 800, 3), np.uint8)

cv2.namedWindow(winname='myimage')
cv2.setMouseCallback('myimage',do_circle)

while True:
    cv2.imshow('myimage',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()
