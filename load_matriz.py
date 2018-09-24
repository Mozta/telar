from PIL import Image
import numpy as np

def patrones():
    n = z = 5
    t1 = np.zeros((n,n), dtype=int)
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
    result = np.arange(100).reshape(10, 10)
    n = 5
    for i in range(n-1):
        print(promedios[i])
    t = 255/(n-1)
    print(t)

    for i in range(n-1):
        if promedios[i] < t:
            print("Matriz "+ str(i) + " pertenece a patron: " +str(0)+" - "+ str(t))
            for j in range(0,n):
                for i in range(0,n):
                    result[j][i] = patrones[0][j][i]
        elif promedios[i] < t*2:
            print("Matriz "+ str(i) + " pertenece a patron: "+str(1)+" - " + str(t*2))
            for j in range(n,n*2):
                for i in range(0,n):
                    result[j][i] = patrones[1][j-n][i-n]
        elif promedios[i] < t*3:
            print("Matriz "+ str(i) + " pertenece a patron: "+str(2)+" - " + str(t*3))
            for j in range(n*2,n*3):
                for i in range(0,n):
                    result[j][i] = patrones[2][j-n*2][i-n*2]
        elif promedios[i] < t*4:
            print("Matriz "+ str(i) + " pertenece a patron: "+str(3)+" - " + str(t*4))
            for j in range(n*3,n*4):
                for i in range(0,n):
                    result[j][i] = patrones[3][j-n*3][i-n*3]
    print(result)


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
