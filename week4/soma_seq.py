tamanho = int(input("Digite o tamanho da sequência de números: "))
soma = 0
contador=0
while contador < tamanho:
    valor = float(input("digite um valor a ser somado:"))
    soma = soma + valor
    contador=contador+1
print("A soma dos valores digitados é: ", soma)
