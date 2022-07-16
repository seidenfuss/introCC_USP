def clone(lista):
    clone=[]
    for objeto in lista:
        clone.append(objeto)
    return clone

lista1=[1,2,3,4,5,6]
lista2=clone(lista1)
lista2[0]=8
print(lista1)
print(lista2)

#outra forma de clonar uma lista é utilizando o fatiamento:
lista2=lista1[0:5]
lista2=lista1[0:]
lista2=lista1[:5]
lista2=lista1[:] #clone

#todas as formas acima significam o mesmo intervalo