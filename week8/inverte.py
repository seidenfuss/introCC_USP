lista=[]
n=1
while n!=0:
    n=int(input("Digite um número: "))
    lista.append(n)

del lista[-1]

lista_reverse=lista[::-1]

for item in lista_reverse:
    print(item)
