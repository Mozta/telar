import numpy as np

n = z = 15
t1 = np.zeros((n,n), dtype=int)
#t1 = t1.tolist()
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
    #print(patrones[j])
    #print("-------------------------")
    if(n%2!=0):
        m+=1

for i in range(n-1):
    patrones1.append(p[z:z+n])
    z+=n

for j in range(n-1):
    print(patrones1[j])
    print("-------------------------")
