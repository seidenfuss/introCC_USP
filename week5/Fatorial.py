def Fatorial(n):
    fat=1
    while n>1:
        fat=fat*n
        n=n-1
    return fat

def testa_fatorial():
    if Fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona para 0")
    if Fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não funciona para 1")
    if Fatorial(2) == 2:
        print("Funciona para 2")
    else:
        print("Não funciona para 2")
    if Fatorial(5) == 120:
        print("Funciona para 5")
    else:
        print("Não funciona para 5")
