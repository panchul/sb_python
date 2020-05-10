# pip install opencv-python 
# pip install pillow 
# The zbar DLLs are included with the Windows Python wheels. On other operating systems,
# you will need to install the zbar shared library.
#  Mac OS X: brew install zbar
#  Linux: 
# sudo apt-get install libzbar0
# pip install pyzbar
# Window :
#  pip install pyzbar

import cv2
from pyzbar import pyzbar
from PIL import Image

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        barcode_text = barcode.data.decode('utf-8')
        print(barcode_text)
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
    return frame

def main():
    selected_camera_index = 0
    camera = cv2.VideoCapture(selected_camera_index)
    ret, frame = camera.read()
    while ret or 1 :
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow('Barcode reader', frame) # Shows the image
        key_pressed = (cv2.waitKey(1) & 0xFF)

        if key_pressed & 0xFF == 27:     # Esc key stops the loop
            break

        if key_pressed == 32:     # 'space' to increase camera index
            selected_camera_index = selected_camera_index + 1
            camera.release()
            camera = cv2.VideoCapture(selected_camera_index)

    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
