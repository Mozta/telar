from PIL import Image
import numpy as np

#255 es blanco
#0 es negro

img = Image.open("lenna.png")
#img = Image.open("mario.jpg")

out = img.resize((160, 160))
#out.show()
im = out.convert("1")
im.show()
#im.save("3.bmp")

l = list(im.getdata())
print(l[:10])


box = (0,0,5,5)
region = im.crop(box)
region.show()

region = region.transpose(Image.ROTATE_180)
im.paste(region, box)
im.show()

new = Image.new('RGB', (160,160), (255, 255, 255))

new = Image.new('1', (160,160), (255))
