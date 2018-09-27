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
    img_array = []

    data_format = np.array(data).reshape(160,160)
    p = r = 0

    for q in range(int(160/n)):
        for k in range(int(160/n)):
            b = []
            for j in range(r,r+n):
                for i in range(p,p+n):
                    b.append(data_format[j][i])
            c = np.array(b).reshape(n,n)
            promedios.append(c.mean())
            img_array.append(c)
            print(c)
            print(c.mean())
            p += n
        r += n
        p = 0
    return promedios, img_array

def satin(n, patrones, promedios, img_array):
    result = np.zeros((160,160), dtype=np.uint8)
    t = 255/(n-1)
    print("Tramo: " + str(t))

    pi = 0
    #Indice horizontal
    z = 0
    #contador de indice total
    cit = 0

    for i in range(len(promedios)):
        for ti in range(n-1):
                if promedios[i] < (t*(ti+1)):
                    print("Matriz "+ str(i) + " pertenece a patron: " +str(ti)+" - "+ str(t*(ti+1)))
                    img_array[i] = patrones[ti-1]
                    break

    img_vector = []
    p0 = 0
    p1 = int(160/n)
    #Recorre los siguientes tramos
    for k in range((int(160/n))):
        #Recorre la matriz hacia abajo
        for j in range (n):
            #Recorre la matriz hacia los lados
            for i in range (p0,p1):
                img_vector = img_vector + list(img_array[i][j])
        p0 = p1
        p1 = p1 + int(160/n)

    data_format = np.array(img_vector, dtype=np.uint8).reshape(160,160)

    np.savetxt("salida2", data_format, fmt="%d")

    print(result)
    img = Image.fromarray(data_format)
    #t = list(img.getdata())
    img.save('mario2.jpg')
    img.show()
    print(img_vector)


#Cargar imagen
img = load_image("mario.jpg")
#Definir tamano de satin
n = 8
#Pasarla a BN
img_ = convert_image(img)
#Genrarar patrones
patrones = patrones(n)
#Calcular promedios
#print(promedios(5,list(img_.getdata())))
promedios, img_array = promedios(n,list(img_.getdata()))
#Aplicar regla satin
satin(n, patrones, promedios, img_array)
