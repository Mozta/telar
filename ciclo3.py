import numpy as np

n = 6
t1 = np.zeros((n,n), dtype=int)
#t1 = t1.tolist()
patrones = []

m = 0
for j in range(n-1):

    for i in reversed(range(n)):
        t1[m][i] = 255
        #print(str(m) +","+ str(i))
        if m < n-2:
            m+=2
        else:
            if m == n-1:
                if(n%2==0):
                    m=0
                else:
                    m=1
            else:
                if(n%2==0):
                    m=1
                else:
                    m=-1
        if i == n/2:
            m+=3

    patrones.append(t1)
    print(patrones[j])
    print("-----------------------")
    m=j+1
