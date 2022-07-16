primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(primos)
##fatias de listas
print(primos[1:2])
#os dois pontos nos 
# indica que estamos 
# trabalhando em um 
# intervalo de indíces
print(primos[2:7])
print(len(primos))
print(primos[0:12])
print(primos[12:25])
# se inicia no primeiro indice
print(primos[:12])
# se termina no ultimo indice
final=primos[12:]
print(final)

if final == primos[12:]:
    print("é igual")

## clonando listas

lista1=["vermelho","verde","azul"]
lista2=lista1
lista2[0] = "rosa"
#desta forma ambas listas são alteradas
print(lista1)
print(lista2)


