
def nao_primo(n):
    i=1
    naoprimo=False

    while i<n-1 and not naoprimo:
        i=i+1
        resto=n%i
        if resto==0:
            naoprimo=True
    return naoprimo

def maior_primo(n):
    i=1
    while i <= n:
        if nao_primo(i) == False:
            maior_primo=i
        i=i+1
    return maior_primo
        
