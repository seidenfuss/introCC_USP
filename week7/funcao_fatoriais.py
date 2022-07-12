
def fatorial(n):
    if n<0:
        fat="não existe fatorial de número negativo"
        return fat
    fat=1
    while n>0:
        fat=fat*n
        n=n-1
    return fat
    
def main():
    n=1
    while n >= 0:
        n=int(input("digite um número inteiro positivo: "))
        print(fatorial(n))
main()
