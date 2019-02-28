from PIL import Image
im = Image.open("0.jpg")
im.show

im_rotate = im.rotate(90)
im_rotate.show