import numpy as np

n = 6
t1 = np.zeros((n,n), dtype=int)
#t1 = t1.tolist()
patrones = []

m = 0
for j in range(n-1):
    for i in range(n):
        t1[m][i] = 255
        print(str(m) +","+ str(i))
        m+=2
        if m == n:
            print("Soy igual")
            m=0
        if i==n-1 and m <= n:
            print("Soy igual y entre")
            m=0
        if m > n:
            print("Soy mayor")
            m=1
    print("---------")
    t = np.fliplr(t1)
    patrones.append(t)
    t="NaN"
    print(patrones[j])
    #print("\n")
    m+=1

for i in range(n-1):
    print(patrones[i])
    print("\n")
#print(t1)
#print(np.fliplr(t1))


#for i in range(n-1, -1, -1):
#    t1[i][m] = 255
#    m+=2
#    if m >= n:
