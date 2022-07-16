L=int(input("Digite a largura: "))
A=int(input("Digite a altura: "))


print(L*"#")
if A>2:
    i=2
    while i<A:
        print("#"+(L-2)*" "+"#")
        i=i+1
print(L*"#")