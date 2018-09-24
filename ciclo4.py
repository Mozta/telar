import numpy as np

def generate_shapes(n):
    t1 = np.zeros((n,n), dtype=int)
    #t1 = t1.tolist()
    patrones = []

    m = 0
    for j in range(n-1):
        for i in reversed(range(n)):
            t1[m][i] = 255
            m += 3 if i == n/2 else 2
            if m > n-1:
                m = m - n
        patrones.append(t1)
        print(patrones[j])
        print("-------------------------")
        if(n%2!=0):
            m+=1
    return np.array(patrones)

print (generate_shapes(5))
