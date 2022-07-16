import math

n=int(input("numero: "))

def e_hipot(h):
    
    if ((h**2) % h) == 0 and h <= n :
        return True
    else:
        return False

def soma_hipot(n):
    soma=0
    i=0
    j=0
    while i<=n:
        i=i+1
        while j<=n:
            j=j+1
            h = math.sqrt(i**2+j**2)
            if e_hipot(h):
                soma=soma+h    
        j=0
    return soma

print(soma_hipot(n))

    