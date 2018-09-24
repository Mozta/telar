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

def patrones(n):
    z = n
    t1 = np.zeros((n,n), dtype=np.uint8)
    t1 = t1.tolist()
    patrones = []
    patrones1 = []
    p = t1

    m = 0
    for j in range(n-1):
        for i in reversed(range(n)):
            t1[m][i] = 255
            m += 3 if i == n/2 else 2
            if m > n-1:
                m = m - n
        patrones.append(t1)
        p = np.append(p, t1,0)
        if(n%2!=0):
            m+=1

    for i in range(n-1):
        patrones1.append(p[z:z+n])
        z+=n
    return patrones1

def promedios(n,data):
    promedios = []
    data_format = np.array(data).reshape(160,160)
    p = r = 0

    for k in range(int(160/n)):
        b = []
        for j in range(0,n):
            for i in range(p,p+n):
                b.append(data_format[j][i])
        c = np.array(b).reshape(n,n)
        promedios.append(c.mean())
        print(c)
        print(c.mean())
        p+=n
    print("Soy p: "+str(p))
    #print(len(promedios))
    return promedios


#Cargar imagen
img = load_image("lenna.png")
#Pasarla a BN
img_ = convert_image(img)
#Genrarar patrones
patrones(5)
#Calcular promedios
print(promedios(5,list(img_.getdata())))
