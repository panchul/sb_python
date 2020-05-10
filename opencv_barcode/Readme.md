# barcode reading demo

See more in my OpenCV notes: 

 - https://github.com/panchul/workspace/blob/master/doc/OpenCV.md
 - https://github.com/panchul/workspace/blob/master/doc/ComputerVision.md
 - https://github.com/panchul/workspace/blob/master/doc/MachineLearning.md

To install pre-reqs:

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

To play around in Python command line:

    >>> from pyzbar import pyzbar
    >>> from PIL import Image
    >>> info = pyzbar.decode(Image.open('sample_barcode.png'))
    >>> print(info)
    [Decoded(data=b'https://barcodesegypt.com', type='QRCODE', rect=Rect(left=190, top=97,
    width=76, height=76), polygon=[Point(x=190, y=97), Point(x=190, y=173), Point(x=266, y=173),
    Point(x=266, y=97)]), Decoded(data=b'https://www.samsung.com/au/support/', type='QRCODE',
    rect=Rect(left=193, top=6, width=72, height=72), polygon=[Point(x=193, y=6), Point(x=193,
    y=77), Point(x=265, y=78), Point(x=264, y=6)]), Decoded(data=b'https://l.ead.me/api-1',
    type='QRCODE', rect=Rect(left=370, top=3, width=77, height=77), polygon=[Point(x=370, y=3),
    Point(x=371, y=80), Point(x=446, y=79), Point(x=447, y=4)]),
    Decoded(data=b'http://en.m.wikipedia.org', type='QRCODE', rect=Rect(left=17, top=15,
    width=147, height=147), polygon=[Point(x=17, y=15), Point(x=17, y=162), Point(x=164,
    y=162), Point(x=164, y=15)])]


To run the program:

    $ python barcode_reader.py
    
To stop it, press `Esc` in the camera window.

