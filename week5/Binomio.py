def Fatorial(n):
    fat=1
    while n>1:
        fat=fat*n
        n=n-1
    return fat

def Binomio(n,k):
    return Fatorial(n)/(Fatorial(k)*Fatorial(n-k))
for j in range (1,10):
    print(Binomio(10,j))

"criar teste automatizado para a função numero binomial"

