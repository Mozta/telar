from PIL import Image
import numpy as np

def patrones():
    n = z = 5
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

def asignaciones(patrones, promedios):
    result = np.arange(100, dtype=np.uint8).reshape(10, 10)
    n = 5
    for i in range(n-1):
        print(promedios[i])
    t = 255/(n-1)
    print(t)

    for i in range(n-1):
        if promedios[i] < t:
            print("Matriz "+ str(i) + " pertenece a patron: " +str(0)+" - "+ str(t))
            if i == 0:
                for i in range(n):
                    result[i][0:n] = patrones[0][i]
            elif i == 1:
                for i in range(n):
                    result[i][n:n*2] = patrones[0][i]
            elif i == 2:
                for i in range(n):
                    result[i+n][0:n] = patrones[0][i]
            elif i == 3:
                for i in range(n):
                    result[i+n][n:n*2] = patrones[0][i]
        elif promedios[i] < t*2:
            print("Matriz "+ str(i) + " pertenece a patron: "+str(1)+" - " + str(t*2))
            if i == 0:
                for i in range(n):
                    result[i][0:n] = patrones[1][i]
            elif i == 1:
                for i in range(n):
                    result[i][n:n*2] = patrones[1][i]
            elif i == 2:
                for i in range(n):
                    result[i+n][0:n] = patrones[1][i]
            elif i == 3:
                for i in range(n):
                    result[i+n][n:n*2] = patrones[1][i]
        elif promedios[i] < t*3:
            print("Matriz "+ str(i) + " pertenece a patron: "+str(2)+" - " + str(t*3))
            if i == 0:
                for i in range(n):
                    result[i][0:n] = patrones[2][i]
            elif i == 1:
                for i in range(n):
                    result[i][n:n*2] = patrones[2][i]
            elif i == 2:
                for i in range(n):
                    result[i+n][0:n] = patrones[2][i]
            elif i == 3:
                for i in range(n):
                    result[i+n][n:n*2] = patrones[2][i]
        elif promedios[i] < t*4:
            print("Matriz "+ str(i) + " pertenece a patron: "+str(3)+" - " + str(t*4))
            if i == 0:
                for i in range(n):
                    result[i][0:n] = patrones[3][i]
            elif i == 1:
                for i in range(n):
                    result[i][n:n*2] = patrones[3][i]
            elif i == 2:
                for i in range(n):
                    result[i+n][0:n] = patrones[3][i]
            elif i == 3:
                for i in range(n):
                    result[i+n][n:n*2] = patrones[3][i]
    print(result)
    img = Image.fromarray(result)
    t = list(img.getdata())

    for i in range(10):
        print(t[i*10:(i+1)*10])
    img.show()


n = 10
p = 0
r = 0
a = result = np.arange(100).reshape(n, n)
promedios = []
#a = np.zeros((n,n), dtype=int)
#for j in range(5):
#    for i in range(5):
#        a[j][i] = 255
print(a.mean())
print(a)
print("\n")

for q in range(2):
    for k in range(2):
        b = []
        for j in range(r,r+5):
            for i in range(p,p+5):
                b.append(a[j][i])
        c = np.array(b).reshape(5,5)
        print(c.mean())
        promedios.append(c.mean())
        print(c)
        p+=5
    p = 0
    r+=5

print(patrones())
asignaciones(patrones(), promedios)

#img = Image.fromarray(data, 'L')
