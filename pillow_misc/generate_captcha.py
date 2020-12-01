#
# Discussion about saving an image
#
# https://stackoverflow.com/questions/902761/saving-a-numpy-array-as-an-image/21034111#21034111
#

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from skimage import transform as tf

def create_captcha(text, shear=0, size=(100,24)):
    im = Image.new("L", size, "black")
    draw = ImageDraw.Draw(im)
    #font = ImageFont.truetype(r"Coval.otf", 22)
    font = ImageFont.truetype(r"/Library/Fonts/Arial Unicode.ttf", 22)
    draw.text((2, 2), text, fill=1, font=font)
    image = np.array(im)
    affine_tf = tf.AffineTransform(shear=shear)
    image = tf.warp(image, affine_tf)
    return image / image.max()

#%matplotlib inline
from matplotlib import pyplot as plt
image_array = create_captcha("GENE", shear=0.5)

#import scipy.misc
#scipy.misc.imsave('outfile.jpg', image_array)

#import scipy.misc
#scipy.misc.toimage(image_array, cmin=0.0, cmax=...).save('output.jpg')

#im = Image.fromarray(image_array)
#im.save("output.jpg")

def write_png(buf, width, height):
    """ buf: must be bytes or a bytearray in Python3.x,
        a regular string in Python2.x.
    """
    import zlib, struct

    # reverse the vertical line order and add null bytes at the start
    width_byte_4 = width * 4
    raw_data = b''.join(
        b'\x00' + buf[span:span + width_byte_4]
        for span in range((height - 1) * width_byte_4, -1, - width_byte_4)
    )

    def png_pack(png_tag, data):
        chunk_head = png_tag + data
        return (struct.pack("!I", len(data)) +
                chunk_head +
                struct.pack("!I", 0xFFFFFFFF & zlib.crc32(chunk_head)))

    return b''.join([
        b'\x89PNG\r\n\x1a\n',
        png_pack(b'IHDR', struct.pack("!2I5B", width, height, 8, 6, 0, 0, 0)),
        png_pack(b'IDAT', zlib.compress(raw_data, 9)),
        png_pack(b'IEND', b'')])

def saveAsPNG(array, filename):
    import struct
    if any([len(row) != len(array[0]) for row in array]):
        raise ValueError # , "Array should have elements of equal size"

    #First row becomes top row of image.
    flat = []; map(flat.extend, reversed(array))
    #Big-endian, unsigned 32-byte integer.
    buf = b''.join([struct.pack('>I', ((0xffFFff & i32)<<8)|(i32>>24) )
                    for i32 in flat])   #Rotate from ARGB to RGBA.

    data = write_png(buf, len(array[0]), len(array))
    f = open(filename, 'wb')
    f.write(data)
    f.close()

#saveAsPNG([[0xffFF0000, 0xffFFFF00],
#           [0xff00aa77, 0xff333333]], 'test_grid.png')
