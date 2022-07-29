import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")
    
    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))
    
    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):

    Sab=[]
    S_ab=0
    
    for i in range(0,5):
        Sab.append(abs(as_a[i]-as_b[i]))
    
    for item in Sab:
        S_ab=S_ab+item
    S_ab=S_ab/6
    return S_ab

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    tamanho_palavras_lista= []
    numero_palavras=[]
    numero_palavras_diferentes=[]
    numero_palavras_unicas=[]
    numero_sentencas=[]
    numero_frases=[]

    tamanho_palavras=0
    tamanho_palavras_total=0
    numero_palavras_total=0
    numero_palavras_diferentes_total=0
    numero_palavras_unicas_total=0
    numero_sentencas_total=0
    numero_frases_total=0

    sentencas=separa_sentencas(texto)
    numero_sentencas.append(len(sentencas))
    
    for sentenca in sentencas:
        frases=separa_frases(sentenca)
        numero_frases.append(len(frases))
    
        for frase in frases:
            lista_palavras=separa_palavras(frase)

            numero_palavras.append(len(lista_palavras))
            numero_palavras_diferentes.append(n_palavras_diferentes(lista_palavras))
            numero_palavras_unicas.append(n_palavras_unicas(lista_palavras))
    
            tamanho_palavras=0
    
            for palavra in lista_palavras:
                tamanho_palavras=tamanho_palavras+len(palavra)
            tamanho_palavras_lista.append(tamanho_palavras)



    for item in tamanho_palavras_lista:
        tamanho_palavras_total=tamanho_palavras_total+item
    for item in numero_palavras:
        numero_palavras_total=numero_palavras_total+item
    for item in numero_palavras_diferentes:
        numero_palavras_diferentes_total=numero_palavras_diferentes_total+item
    for item in numero_palavras_unicas:
        numero_palavras_unicas_total=numero_palavras_unicas_total+item
    for item in numero_frases:
        numero_frases_total=numero_frases_total+item
    for item in numero_sentencas:
        numero_sentencas_total=numero_sentencas_total+item    


# wal = soma dos tamanhos das palavras / numero total de palavras
    wal=tamanho_palavras_total/numero_palavras_total

#    ttr = numero de palavras diferentes / numero total de palavras
    ttr=numero_palavras_diferentes_total/numero_palavras_total

#    hlr = palavras unicas / total de palavras
    hlr=numero_palavras_unicas_total/numero_palavras_total

#    sal = soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças [sem os separadores == [,:;]]
    sal = tamanho_palavras_total/numero_sentencas_total

#    sac = número total de frases divido pelo número de sentenças.
    sac = numero_frases_total/numero_sentencas_total

#    pal = soma do número de caracteres em cada frase dividida pelo número de frases no texto
    pal = tamanho_palavras_total/numero_frases_total
    
    return [wal,ttr,hlr,sal,sac,pal]
 
def avalia_textos(textos, ass_cp):

   

    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    S_ab=[]
    for texto in textos:
        ass_txt=calcula_assinatura(texto)
        S_ab.append(compara_assinatura(ass_cp,ass_txt))

    menor=S_ab[0]
    c=0

    for item in S_ab:
        c+=1
        if item<menor:
            menor=item
    
    return print("O autor do texto", c,"está infectado com COH-PIAH")

ass_cp=le_assinatura()
textos=le_textos()


avalia_textos(textos,ass_cp)

