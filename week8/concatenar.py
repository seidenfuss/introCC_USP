#concatena listas e cria uma nova lista 
# com todos os elementos

lista1 = [1,2] + [3,4]
lista2= [5,6,7]
lista3=lista1+lista2

print(lista1)
print(lista2)
print(lista3)
print([4,5,6,3,2,8]+[0,7,6,5,3,1])

#append: diferente de concatenação
#append altera uma lista existente 
#enquanto a concatenaçao cria uma lista nova
#sem alterar as listas existentes

lista2.append(8)
print(lista2)

#multiplicando (repetindo) listas

lista_duplicada=lista1*2
print(lista_duplicada)

#remoção de elementos em listas:
del lista1[1]
print(lista1)

del lista3[1:4]
print(lista3)
