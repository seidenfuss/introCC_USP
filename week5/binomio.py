def Fatorial(n):
    fat=1
    while n>1:
        fat=fat*n
        n=n-1
    return fat

def binomio(n,k):
    return Fatorial(n)/(Fatorial(k)*Fatorial(n-k))

for i in range(1,10):
    print(binomio(10,i))

"criar teste automatizado para a função numero binomial"

