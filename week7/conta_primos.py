
def n_primos(n):
    if n>=2:
        i=2
        cont=0
        while i<=n:
            fator=2
            while i % fator != 0 and fator <= i/2:
                fator=fator+1
            if i % fator != 0 or i==2:
                primo=True
                cont=cont+1
            else:
                primo=False
            i=i+1
    return cont