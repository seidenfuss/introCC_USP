def fatorial(n):
    i=0
    produto=1
    if n!=0:
        while i<n:
            i=i+1
            produto=produto*i
    return produto

def binomio(n,k):
    return fatorial(n)/(fatorial(k)*fatorial(n-k))


