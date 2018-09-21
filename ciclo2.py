import numpy as np

n = 6
t1 = np.zeros((n,n), dtype=int)
#t1 = t1.tolist()
patrones = []

m = 0
for j in range(n-1):
    for i in reversed(range(n)):
        t1[m][i] = 255
        print(str(m) +","+ str(i))
        if i == n/2:
            m+=3
        else:
            m+=2

        if m > n-1:
            m = m - (n)
    patrones.append(t1)
    print(patrones[j])

    if(n%2!=0):
        m+=1
