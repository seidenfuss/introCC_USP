def remove_repetidos(lista):
    nova_lista=[]
    lista.sort()
    for item in lista:
        if item not in nova_lista:
            nova_lista.append(item)
    return nova_lista

