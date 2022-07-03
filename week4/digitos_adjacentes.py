numero=int(input("digite um numero inteiro  grande: "))

adjIguais = False
soma = 0;

while ((numero//10 != 0) or (numero%10 != 0)) and ( not adjIguais):
    digito1=numero%10
    numero=numero//10
    digito2=numero%10

    if digito1 == digito2:
        adjIguais = True

if adjIguais:
    print("sim")
else:
    print("não")