numero=int(input("Digite um numero inteiro: "))
soma = 0;
while (numero//10 != 0) or (numero%10 != 0):
    digito=numero%10
    numero=numero//10
    soma=soma+digito
print(soma)