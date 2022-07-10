#n = numero total de peças
#m = numero máximo de peças que podem ser retirados

def computador_escolhe_jogada(n,m):

    k=1
    while k<=m:
        resta=n-k
        if resta%(m+1)==0:
            remove=k
            break
        else:
            remove=m
        k=k+1

    if remove==1:
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou",remove,"peças.")
    
    if resta == 1:
        print("Agora resta apenas uma peça no tabuleiro.","\n")
    elif resta<=0:
        print("Fim do jogo! O computador ganhou!","\n")
    else:
        print("Agora restam",resta,"peças no tabuleiro.","\n")
    return remove

def usuario_escolhe_jogada(n,m):
    remove = int(input("Quantas peças você vai tirar? "))
    
    while remove>m or remove<=0:
        print("\n","Oops! Jogada inválida! Tente de novo.","\n")
        remove = int(input("Quantas peças você vai tirar? "))
    
    resta = n-remove
    
    if remove==1:
        print("\n","Você tirou uma peça.")
    else:
        print("\n","Você tirou",remove,"peças.")
    
    if resta == 1:
        print("Agora resta apenas uma peça no tabuleiro.","\n")
    elif resta<=0:
        print("Fim do jogo! Você ganhou!","\n")
    else:
        print("Agora restam",resta,"peças no tabuleiro.","\n")
    return remove

def partida():

    n=int(input("Quantas peças? "))
    m=int(input("Limite de peças por jogada? "))
    
    while n<m:
        n=int(input("Quantas peças? "))
        m=int(input("Limite de peças por jogada? "))

    if n%(m+1)==0:
        print("\n Você começa! \n")
        computador=False
    else:
        print("\n Computador começa! \n")
        computador=True
       
    while n>0:
        if computador:
            remove = computador_escolhe_jogada(n,m)
            vencedor= computador
            n = n-remove
            computador=False
        elif not computador:
            remove = usuario_escolhe_jogada(n,m)
            vencedor= not computador
            n = n-remove
            computador=True
    return vencedor

def campeonato():
    
    rodada=1
    computador=0 #computador
    usuario=0 #usuario

    while rodada<=3:
        print("**** Rodada",rodada,"****","\n")
        vencedor=partida()      
        rodada=rodada+1
        
            #placar
        if vencedor:
            computador=computador+1
        elif not vencedor:
            usuario=usuario+1

    print("**** Final do Campeonato! ****","\n")
    print("Placar: Você",usuario,"X",computador,"Computador")

def main():
    print("\n","Bem-vindo ao jogo do NIM! Escolha:","\n")
    modo_jogo=int(input("1 - para jogar uma partida isolada \n2 - para jogar um campeonato 2 \n "))
    if modo_jogo==1:
        print("\n","Você escolheu uma partida isolada!")
        partida()
    if modo_jogo==2:
        print("\n","Você escolheu um campeonato!")
        campeonato()
    return

main()
