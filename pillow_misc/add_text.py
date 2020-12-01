from PIL import Image, ImageFont, ImageDraw

im_in = Image.open("input.jpg")
my_font=ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf",150)
#my_font=ImageFont.truetype("arial.ttf",150)
my_text="some text"
im_editable=ImageDraw.Draw(im_in)
im_editable.text((200,200),my_text,(240,240,240),font=my_font)
im_in.save("output.jpg")

