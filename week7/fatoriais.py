
def main():
    n=int(input("digite um número inteiro positivo: "))
    while n >= 0:
        fat = 1
        while n>1:
            fat=fat*n
            n=n-1
        print(fat)
        n=int(input("digite um número inteiro positivo: "))
main()
