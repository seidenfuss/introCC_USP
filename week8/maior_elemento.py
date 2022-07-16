def maior_elemento(lista):

    maior=lista[0]

    for item in lista:
        if item>maior:
            maior=item
    return maior