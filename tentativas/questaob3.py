# Olá. Crie um código em python que
# receba um numero inteiro - que representa
# a quantidade de pessoas em um grupo - e uma
# lista de inteiros - que representa cada pessoa
# desse grupo, considerando que podem ser dígitos
# repetidos e mesmo assim são considerados pessoas diferentes. O código deve mostrar todas as formas possíveis de dividir esse grupo em pares, por exemplo: se for um grupo de 4 pessoas, mostrar as 3 formas de dividir esse grupo em 2 pares.

# ler entradas
N = int(input())
alturas = input()

#formatar alturas para lista de inteiros
alturas = [int(i) for i in alturas.split(" ")]
#print(alturas)

# ...
primeiros_pares = []

for index1, i in enumerate(alturas):
    for index2, j in enumerate(alturas):
        if index1 != index2:
