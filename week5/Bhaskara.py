import math

def Delta(a,b,c):
    return b ** 2 - 4 * a * c

def Raiz1(a,b,c):
    return (-b + math.sqrt(Delta(a,b,c)))/(2*a)

def Raiz2(a,b,c):
    return (-b - math.sqrt(Delta(a,b,c)))/(2*a)

def Crescente(raiz1, raiz2):
        if raiz1 > raiz2:
            r1 = raiz2
            r2 = raiz1
        else:
            r1=raiz1
            r2=raiz2
        return print("as raízes da equação são", r1,"e",r2)

def Bhaskara(a,b,c):
    if Delta(a,b,c) > 0:
        raiz1 = Raiz1(a,b,c)
        raiz2 = Raiz2(a,b,c)
        return Crescente(raiz1, raiz2)
    elif Delta(a,b,c) == 0:
        raiz1 = Raiz1(a,b,c)
        return print("a raiz desta equação é", raiz1)
    else:
        return print("esta equação não possui raízes reais")

print("exemplo sem raízes reais:")
Bhaskara(1,2,3)

print("exemplo com duas raízes:")
Bhaskara(5,10,4)

print("exemplo com uma raiz:")
Bhaskara(1,2,1)