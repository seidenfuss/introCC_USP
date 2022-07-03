n=int(input("Digite um número inteiro: "))
i=1
naoprimo=False

while i<n-1 and not naoprimo:
    i=i+1
    resto=n%i
    if resto==0:
        naoprimo=True

if naoprimo:
    print("não primo")
else:
    print("primo")