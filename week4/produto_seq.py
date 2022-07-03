tamanho = int(input("Digite o tamanho da sequência de números: "))
produto = 1
contador=0
while contador < tamanho:
    valor = float(input("digite um valor a ser multiplicado:"))
    produto = produto * valor
    contador=contador+1
print("o produto dos valores digitados é: ", produto)
