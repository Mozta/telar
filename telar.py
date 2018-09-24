from PIL import Image
import numpy as np
#255 es blanco
#0 es negro

def load_image(source):
    img = Image.open(source)
    return img.resize((160, 160))

def convert_image(source):
    return source.convert("L")

def binariza(source):
    umbral = 120
    datos = source.getdata()
    datos_binarios = []
    for x in datos:
        if x < umbral:
            datos_binarios.append(0)
        else:
            datos_binarios.append(255)
    nueva_imagen = Image.new('L', (160,160), (255))
    nueva_imagen.putdata(datos_binarios)

img = load_image("lenna.png")

img_ = convert_image(img)

img_.show()
#im.save("3.bmp")

datos = list(img_.getdata())
print(datos)
