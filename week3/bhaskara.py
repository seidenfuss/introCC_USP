import math

a=float(input("digite o coeficiente a: "))
b=float(input("digite o coeficiente b: "))
c=float(input("digite o coeficiente c: "))

delta = b ** 2 - 4 * a * c

if delta > 0:
    raiz1= (-b + math.sqrt(delta))/(2*a)
    raiz2= (-b - math.sqrt(delta))/(2*a)

    if raiz1 > raiz2:
        r1 = raiz2
        r2 = raiz1
    else:
        r1=raiz1
        r2=raiz2
    print("as raízes da equação são", r1,"e",r2)
    
elif delta == 0:
    raiz1= (-b + math.sqrt(delta))/(2*a)
    print("a raiz desta equação é", raiz1)
    
else:
    print("esta equação não possui raízes reais")
