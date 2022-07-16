import math

n=int(input("numero: "))

def e_hipot(n):
    i=0
    j=0
    while i<=n:
        i=i+1
        while j<=n:
            j=j+1
            h = math.sqrt(i**2+j**2)
            if ((h**2) % h) == 0 and h <= n :
                print(i,j,h**2,h)
        j=0
    return h

e_hipot(n)
